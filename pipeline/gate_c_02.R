# Unit 02 — Gate C. CNR1 detection in frozen ADPKD PT only.
# Do not compute ADPKD vs control. Do not load GSE195460. Do not change 1% / 100.

SEED <- 20260829L
set.seed(SEED)
suppressPackageStartupMessages(library(Matrix))

args <- commandArgs(trailingOnly = FALSE)
file_arg <- sub("^--file=", "", args[grep("^--file=", args)])
if (!length(file_arg)) {
  stop("Run with Rscript pipeline/gate_c_02.R")
}
root <- normalizePath(file.path(dirname(file_arg), ".."))

rds_path <- file.path(root, "data/derived/GSE185948/count_RNA.rds")
buckets_path <- file.path(root, "data/derived/GSE185948/cell_buckets.csv")
out_dir <- file.path(root, "data/derived/GSE185948")
out_json <- file.path(out_dir, "gate_c_stats.json")
out_md <- file.path(root, "research/02-detection.md")

stopifnot(file.exists(rds_path), file.exists(buckets_path))

buckets <- utils::read.csv(buckets_path, stringsAsFactors = FALSE)
pt <- buckets[buckets$is_pt == 1L, , drop = FALSE]
n_pt <- nrow(pt)
if (n_pt != 23172L) {
  stop("Frozen PT n mismatch: got ", n_pt, " expected 23172 from Unit 01")
}

message("readRDS: ", rds_path)
counts <- readRDS(rds_path)
if (!inherits(counts, "dgCMatrix")) {
  stop("Expected dgCMatrix, got ", paste(class(counts), collapse = "/"))
}
if (!("CNR1" %in% rownames(counts))) {
  stop("CNR1 absent from feature index")
}
if (sum(rownames(counts) == "CNR1") != 1L) {
  stop("CNR1 is not a unique rowname")
}
cnr1_i <- which(rownames(counts) == "CNR1")
neighbor_lo <- if (cnr1_i > 1L) rownames(counts)[cnr1_i - 1L] else "NA"
neighbor_hi <- if (cnr1_i < nrow(counts)) rownames(counts)[cnr1_i + 1L] else "NA"

# Align PT cells to matrix columns via metadata name == colnames
idx <- match(pt$name, colnames(counts))
if (anyNA(idx)) {
  stop("PT cell_id not in matrix colnames: ", sum(is.na(idx)))
}

cnr1 <- as.numeric(counts["CNR1", idx])
n_pos <- sum(cnr1 > 0)
frac <- n_pos / n_pt
cnr1_max_pt <- max(cnr1)
# Full-matrix >0 is a gene-row / join sanity check only. Not Gate C. Not a cell-type claim.
cnr1_all <- as.numeric(counts["CNR1", ])
n_pos_all <- sum(cnr1_all > 0)
n_all <- length(cnr1_all)
rule_n <- n_pt >= 100L
rule_frac <- frac >= 0.01
meets_rule <- rule_n && rule_frac

# Do not write per-cell CNR1 vs disease. Detection only on the pooled PT object.

json <- sprintf(
  paste0(
    "{\n",
    "  \"n_PT\": %d,\n",
    "  \"n_CNR1_pos\": %d,\n",
    "  \"frac_pos\": %.10f,\n",
    "  \"cnr1_max_in_pt\": %.10f,\n",
    "  \"n_all_nuclei\": %d,\n",
    "  \"n_CNR1_pos_all_nuclei\": %d,\n",
    "  \"threshold_frac\": 0.01,\n",
    "  \"threshold_n\": 100,\n",
    "  \"n_ge_100\": %s,\n",
    "  \"frac_ge_1pct\": %s,\n",
    "  \"numbers_meet_KILL_Gate_C_rule\": %s,\n",
    "  \"human_marks_gate\": true,\n",
    "  \"dkd_loaded\": false,\n",
    "  \"cnr1_used_to_define_PT\": false\n",
    "}\n"
  ),
  n_pt, as.integer(n_pos), frac, cnr1_max_pt,
  n_all, as.integer(n_pos_all),
  if (rule_n) "true" else "false",
  if (rule_frac) "true" else "false",
  if (meets_rule) "true" else "false"
)
writeLines(json, out_json, sep = "")
message("wrote ", out_json)

now <- format(as.POSIXct(Sys.time(), tz = "UTC"), "%Y-%m-%d %H:%M UTC")
pct <- sprintf("%.4f", 100 * frac)
md <- c(
  "# Unit 02 — Gate C detection (study 1)",
  "",
  paste0("**Generated:** ", now),
  "**Runner:** `pipeline/gate_c_02.R` (seed `20260829`; detection is deterministic).",
  "**Object:** Frozen GSE185948 PT (`is_pt` from Unit 01: `celltype` ∈ `{PT1, PT2}`, including injured subset).",
  "**Must not (this unit):** change 1% / 100 after seeing Gate A or S; DKD *CNR1*; *CNR1*-defined PT; Gate A contrast.",
  "",
  "## Detection",
  "",
  paste0("- n nuclei in frozen PT / failed-repair object: **", n_pt, "**."),
  paste0("- Nuclei with *CNR1* matrix value > 0: **", as.integer(n_pos), "**."),
  paste0("- Detection fraction: **", sprintf("%.6f", frac), "** (", pct, "%)."),
  paste0("- Max *CNR1* value in frozen PT: **", sprintf("%.4f", cnr1_max_pt), "** (non-integer; deposited `count_RNA` is log-like, not integer UMI)."),
  "- Estimator: indicator value > 0 on the Unit 01 RDS, unweighted over nuclei in the frozen PT object. Same >0 rule as `KILL.md` / `PROTOCOL.md` Gate C. No pseudobulk. No ADPKD vs control split (that is Gate A). No DKD matrix loaded.",
  "",
  "## Diagnostics (not Gate C)",
  "",
  paste0("- *CNR1* is a unique row (neighbors `", neighbor_lo, "`, `", neighbor_hi, "`)."),
  paste0("- Full GSE185948 matrix: **", as.integer(n_pos_all), "** / **", n_all, "** nuclei have *CNR1* > 0 (join and gene-row check only; not a localization claim; not used to change 1% / 100)."),
  "",
  "## Frozen decision rule (`KILL.md` Gate C)",
  "",
  "- Pass if detection ≥ **1%** **and** n ≥ **100**.",
  paste0("- n ≥ 100: **", rule_n, "**."),
  paste0("- fraction ≥ 0.01: **", rule_frac, "**."),
  paste0("- Numbers meet the written rule: **", meets_rule, "**."),
  "- **Gate C mark is human.** Agent does not pass or fail the gate.",
  "",
  "No Gate A/B/S numbers. If the human marks C fail, do not run A or S.",
  "",
  "Human Gate C mark is recorded in `DECIDE.md` / `STATUS.md`, not in this generated file.",
  ""
)
writeLines(md, out_md)
message("wrote ", out_md)
message("frac=", frac, " n_pos=", n_pos, " n_PT=", n_pt, " meets_rule=", meets_rule)
