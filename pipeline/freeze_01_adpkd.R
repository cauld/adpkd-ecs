# Unit 01 — GSE185948 state freeze. Do not compute CNR1 vs cell type or disease.
# Author PT tokens from metadata; injured-PT marker fallback (PROTOCOL).

SEED <- 20260829L
set.seed(SEED)
suppressPackageStartupMessages(library(Matrix))

args <- commandArgs(trailingOnly = FALSE)
file_arg <- sub("^--file=", "", args[grep("^--file=", args)])
if (!length(file_arg)) {
  stop("Run with Rscript pipeline/freeze_01_adpkd.R")
}
root <- normalizePath(file.path(dirname(file_arg), ".."))

rds_path <- file.path(root, "data/derived/GSE185948/count_RNA.rds")
meta_path <- file.path(root, "data/raw/GSE185948/GSE185948_metadata_RNA.csv.gz")
out_dir <- file.path(root, "data/derived/GSE185948")
dir.create(out_dir, recursive = TRUE, showWarnings = FALSE)

inj_genes <- c("VCAM1", "HAVCR1", "PROM1")
# Extract only assignment genes — never CNR1 for this unit.
keep_genes <- inj_genes

message("readRDS: ", rds_path)
gc()
obj <- readRDS(rds_path)
message("class: ", paste(class(obj), collapse = "/"))
message("typeof: ", typeof(obj))

get_counts <- function(x) {
  if (inherits(x, "dgCMatrix") || inherits(x, "dgTMatrix") || inherits(x, "Matrix")) {
    return(x)
  }
  if (is.matrix(x) || is(x, "sparseMatrix")) {
    return(x)
  }
  # Seurat-like S4 without the Seurat package
  if (isS4(x)) {
    slot_names <- methods::slotNames(x)
    message("S4 slots: ", paste(slot_names, collapse = ", "))
    if ("assays" %in% slot_names) {
      assays <- methods::slot(x, "assays")
      message("assays class: ", paste(class(assays), collapse = "/"))
      rna <- NULL
      if (is.list(assays) || is.environment(assays)) {
        rna <- assays[["RNA"]]
        if (is.null(rna) && length(assays)) rna <- assays[[1]]
      }
      if (isS4(rna)) {
        rs <- methods::slotNames(rna)
        message("assay slots: ", paste(rs, collapse = ", "))
        if ("counts" %in% rs) {
          return(methods::slot(rna, "counts"))
        }
        if ("layers" %in% rs) {
          layers <- methods::slot(rna, "layers")
          if (!is.null(layers[["counts"]])) return(layers[["counts"]])
          if (length(layers)) return(layers[[1]])
        }
        if ("data" %in% rs) {
          return(methods::slot(rna, "data"))
        }
      }
    }
    if ("data" %in% slot_names) {
      return(methods::slot(x, "data"))
    }
  }
  stop("Could not locate a counts matrix in the RDS object")
}

counts <- get_counts(obj)
message("counts class: ", paste(class(counts), collapse = "/"))
message("dim: ", paste(dim(counts), collapse = " x "))
rn <- rownames(counts)
cn <- colnames(counts)
message("n_genes: ", length(rn), " n_cells: ", length(cn))
message("head genes: ", paste(head(rn, 8), collapse = ", "))
message("head cells: ", paste(head(cn, 3), collapse = " | "))

present <- keep_genes[keep_genes %in% rn]
missing <- keep_genes[!keep_genes %in% rn]
message("injury genes present: ", paste(present, collapse = ", "))
if (length(missing)) {
  stop("Missing injury genes: ", paste(missing, collapse = ", "))
}

sub <- counts[present, , drop = FALSE]
# counts > 0 only; do not write CNR1
inj_any <- Matrix::colSums(sub > 0) > 0L
inj_n <- as.integer(Matrix::colSums(sub > 0))

cell_tbl <- data.frame(
  cell_id = cn,
  VCAM1_pos = as.integer(if ("VCAM1" %in% present) as.numeric(sub["VCAM1", ] > 0) else NA_integer_),
  HAVCR1_pos = as.integer(if ("HAVCR1" %in% present) as.numeric(sub["HAVCR1", ] > 0) else NA_integer_),
  PROM1_pos = as.integer(if ("PROM1" %in% present) as.numeric(sub["PROM1", ] > 0) else NA_integer_),
  inj_n_genes = inj_n,
  inj_any = as.integer(inj_any),
  stringsAsFactors = FALSE
)

out_csv <- file.path(out_dir, "injury_marker_pos.csv")
utils::write.csv(cell_tbl, out_csv, row.names = FALSE)
message("wrote ", out_csv, " n=", nrow(cell_tbl))

inspect <- file.path(out_dir, "rds_inspect.txt")
writeLines(c(
  paste("class", paste(class(obj), collapse = "/")),
  paste("counts_class", paste(class(counts), collapse = "/")),
  paste("dim", paste(dim(counts), collapse = "x")),
  paste("n_genes", length(rn)),
  paste("n_cells", length(cn)),
  paste("injury_genes", paste(present, collapse = ",")),
  "cnr1_extracted=FALSE"
), inspect)

rm(obj, counts, sub)
gc()
message("done")
