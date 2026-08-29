# Computational and Pharmacological Pathways for Cannabinoid-Mediated Therapeutics in Autosomal Dominant Polycystic Kidney Disease

**Status in this repo:** source briefing. Not a protocol, not confirmatory, not a claims ceiling. v1 kill test is Pathway A only (`QUESTION.md`, `KILL.md`). Pathways B–D are in `EXPLORE.md`.

Archived 2026-08-29 from the study-opening note. Do not treat tables below as frozen gene lists or pass/fail rules.

---

## The molecular and systemic pathophysiology of ADPKD

Autosomal dominant polycystic kidney disease (ADPKD) represents the most prevalent inherited renal disorder and serves as a primary monogenic driver of end-stage kidney disease (ESKD) globally, affecting approximately 1 in 1,000 to 1 in 2,000 individuals. The pathology is predominantly driven by inactivating mutations in the *PKD1* gene, which encodes polycystin-1 and accounts for roughly 85% of cases, or the *PKD2* gene, which encodes polycystin-2 and represents approximately 15% of cases. The polycystin complex localizes to the primary cilium of renal epithelial cells, where it functions as a specialized mechanosensory and chemosensory apparatus responsible for regulating intracellular calcium homeostasis.

A reduction or total loss of polycystin function disrupts this ciliary calcium signaling cascade, triggering a deleterious sequence of downstream intracellular events. Most notably, this dysregulation leads to a massive elevation of intracellular cyclic adenosine monophosphate (cAMP) and the hyperactivation of the mechanistic target of rapamycin (mTOR) pathway. The elevated cAMP levels stimulate protein kinase A (PKA), which subsequently drives transepithelial chloride and fluid secretion into the cyst lumen via the cystic fibrosis transmembrane conductance regulator (CFTR), while simultaneously promoting aberrant, continuous epithelial cell proliferation.

Beyond these localized structural aberrations, ADPKD is increasingly recognized not merely as a localized renal defect, but as a systemic metabolic disorder. Polycystin deficiency induces a fundamental metabolic reprogramming in renal epithelial cells, forcing cellular energy production to shift from highly efficient oxidative phosphorylation toward aerobic glycolysis. This metabolic shift, highly analogous to the Warburg effect observed in malignant oncology, has been thoroughly documented in orthologous murine models, such as *Ksp-Cre;Pkd1 flox/−* mice, which develop early and severe polycystic kidney disease. In these models, defective glycolysis leads to higher localized amounts of ATP and the transcriptional deregulation of key glycolytic enzymes, a process that can be partially ameliorated by the administration of glucose analogs like 2-deoxy-d-glucose (2DG). This shift to aerobic glycolysis is accompanied by severe mitochondrial dysfunction, the accumulation of reactive oxygen species (ROS), and the chronic activation of pro-inflammatory cascades, ultimately resulting in interstitial inflammation, macrophage infiltration, and extensive renal fibrosis.

The current standard of care for rapidly progressive ADPKD relies heavily on tolvaptan, a selective vasopressin V2 receptor (V2R) antagonist. By blocking V2R in the collecting ducts, tolvaptan effectively lowers intracellular cAMP levels, thereby decelerating cyst expansion and slowing the overall decline of renal function. However, the clinical utility of tolvaptan is significantly hampered by severe aquaretic side effects, resulting in massive polyuria, and a well-documented, potentially fatal risk of hepatotoxicity. This liver toxicity is primarily driven by cytochrome P450 metabolism, specifically via the CYP3A4 enzyme, which generates toxic downstream metabolites. This distinct therapeutic bottleneck necessitates the identification of novel, metabolically targeted interventions that can bypass the hepatic toxicity associated with current V2R antagonism while simultaneously addressing the metabolic and inflammatory drivers of the disease.

## Endocannabinoid system dysregulation as a pathogenic driver

Emerging transcriptomic and metabolomic evidence reveals that the endocannabinoid system (ECS)—a highly conserved lipid signaling network governing metabolic homeostasis, nociception, and immune response—is profoundly dysregulated in the context of ADPKD. The ECS is primarily composed of the G-protein-coupled receptors (GPCRs) cannabinoid receptor type 1 (CB1R) and type 2 (CB2R), their endogenous lipid ligands anandamide (AEA) and 2-arachidonoylglycerol (2-AG), and the metabolic enzymes responsible for their synthesis and degradation, such as fatty acid amide hydrolase (FAAH) and monoacylglycerol lipase (MGLL).

Extensive analyses of human ADPKD bulk microarray data (such as the GSE7869 dataset) and single-nucleus RNA-sequencing (snRNA-seq) datasets (such as GSE185948) demonstrate a consistent and marked upregulation of *CNR1*, the gene encoding CB1R, in cystic kidneys when compared to healthy controls. Single-nucleus resolution utilizing advanced sequencing platforms further localizes this *CNR1* enrichment specifically to metabolically stressed, failed-repair proximal tubule epithelial cells. Paradoxically, this massive receptor upregulation is accompanied by a severe depletion of the endogenous ligands AEA and 2-AG in the circulating plasma and local tissue, alongside a significant reduction in the expression of key biosynthetic and metabolizing enzymes, including *FAAH*, *NAPEPLD*, and *MGLL*.

This progressive ECS dysregulation is entirely disease-specific. Comparative transcriptomic analyses against diabetic kidney disease cohorts (such as the GSE195460 dataset) show minimal ECS alterations, highlighting the unique and highly targeted role of this pathway in ADPKD pathogenesis. In orthologous murine models of ADPKD, particularly *Pkd1 RC/RC* mice evaluated at 3, 6, 9, and 12 months, CB1R protein elevation temporally precedes the depletion of endocannabinoid ligands. This timeline suggests a mechanism of progressive receptor sensitization driven by initial cellular stress, followed by a total metabolic collapse of the local endocannabinoid signaling network. Crucially, the degree of ECS dysregulation—specifically the magnitude of CB1R overexpression and AEA/2-AG depletion—correlates robustly with disease severity, overall cyst burden, declining estimated glomerular filtration rate (eGFR), and elevations in blood urea nitrogen (BUN) and creatinine clearance.

The mechanistic implications of this dysregulation are critical to understanding how the disease progresses. Under normal physiological conditions, CB1R primarily couples to Gi/o proteins, which serve to inhibit adenylyl cyclase and, theoretically, reduce intracellular cAMP levels. However, in the context of renal pathology and structural cellular stress, CB1R signaling exhibits functional selectivity and bias toward non-canonical pathways. Upregulated CB1R in these failing proximal tubules drives the activation of β-arrestin-1, Akt, and various mitogen-activated protein kinases (MAPKs), while simultaneously suppressing AMP-activated protein kinase (AMPK). The overactivation of these specific cascades drives fibrogenesis, accelerates epithelial-to-mesenchymal transition (EMT), and exacerbates mitochondrial dysfunction in the renal parenchyma. Therefore, despite its native Gi/o coupling, upregulated CB1R in ADPKD acts as a maladaptive, pro-fibrotic, and pro-inflammatory driver rather than a compensatory cAMP-lowering mechanism.

### Table 1. Endocannabinoid system components and stated alterations in ADPKD

| Component | Normal renal function | Pathological alteration in ADPKD (briefing) | Clinical correlation (briefing) |
|---|---|---|---|
| CB1R (*CNR1*) | Basal hemodynamics and cellular metabolism | Highly upregulated (proximal tubules) | Cyst burden, reduced GFR, interstitial fibrosis |
| CB2R (*CNR2*) | Immune responses and macrophage polarity | Variable expression | Potential anti-inflammatory agonism |
| AEA (anandamide) | Endogenous partial agonist at CB1R/CB2R | Severely depleted | Kidney enlargement / progression |
| 2-AG | Endogenous full agonist at CB1R/CB2R | Severely depleted | Chronic inflammation / pro-fibrotic signaling |
| FAAH / MGLL | Degradation of AEA and 2-AG | Downregulated | Local ECS metabolic collapse |

## Distinguishing phytocannabinoids from synthetic cannabinoids in renal pathology

When evaluating the therapeutic potential of cannabinoids for kidney disease, a rigid distinction must be drawn between naturally occurring phytocannabinoids derived from *Cannabis sativa* and lab-created synthetic cannabinoids (SCBs). The botanical cannabinoids, which include Δ9-tetrahydrocannabinol (THC), cannabidiol (CBD), cannabigerol (CBG), and Δ9-tetrahydrocannabivarin (THCV), possess complex, often partial-agonist or antagonist profiles at the classical CB1 and CB2 receptors.

Conversely, synthetic cannabinoids, frequently sprayed onto plant matter and sold illicitly, act as highly potent, full agonists at both CB1 and CB2 receptors. The epidemiological data surrounding SCBs underscores their severe nephrotoxicity. Clinical clusters of acute kidney injury (AKI) have been repeatedly linked to the inhalation of synthetic cannabinoids, particularly fluorinated compounds such as XLR-11 and potent indole precursors like AM2201. Patients presenting with SCB-induced AKI frequently exhibit acute tubular necrosis (ATN) and acute tubulointerstitial nephritis upon renal biopsy, accompanied by massively elevated serum creatinine levels.

The pathogenesis of this synthetic cannabinoid-induced AKI is believed to be rooted in the overwhelming, non-physiological full agonism of the CB1 receptor in the renal tubules, which rapidly induces cellular toxicity, massive oxidative stress, and rapid-onset apoptosis. This starkly contrasts with the behavior of phytocannabinoids, which, due to their partial agonism or antagonism, do not typically induce acute tubular necrosis in healthy individuals. Understanding this dichotomy is essential; while full, unmitigated synthetic activation of the ECS in the kidney drives acute organ failure, highly targeted, molecule-specific antagonism of the CB1 receptor or selective agonism of the CB2 receptor using phytocannabinoid scaffolds offers (in the briefing’s argument) renoprotective potential.

## Therapeutic blockade of the CB1 receptor

Given that CB1R overactivation in the proximal tubules promotes fibrosis and metabolic dysregulation, CB1R antagonism represents a highly rational therapeutic avenue for ADPKD. The first-in-class CB1R antagonist and inverse agonist, rimonabant (SR141716A), was extensively studied and briefly approved in Europe for the treatment of obesity. Rimonabant demonstrated profound efficacy in reducing body weight, reversing insulin resistance, mobilizing abdominal fat, and attenuating experimental renal and hepatic fibrosis. However, the high lipophilicity of rimonabant allowed it to readily cross the blood-brain barrier (BBB), where it exerted inverse agonism on central CB1 receptors. This central activity led to severe neuropsychiatric adverse events, including clinically significant depression, anxiety, and suicidal ideation, which ultimately resulted in the drug's global market withdrawal and halted the clinical progression of systemic CB1R blockade.

This clinical failure catalyzed the development of peripherally restricted CB1R antagonists. These molecules are specifically engineered with increased polar surface areas or specific molecular weights to prevent BBB penetrance, thereby retaining the metabolic and anti-fibrotic benefits in peripheral organs like the liver and kidneys without engaging the central nervous system. JD5037, a potent, peripherally restricted CB1R inverse agonist, has shown immense preclinical promise. With an inhibitory constant (IC50) ranging from 29 to 148 nM depending on the assay environment, JD5037 effectively mitigates hepatorenal fibrosis, reverses obesity-induced nephropathy, and improves overall metabolic parameters. It achieves this by shifting CB1R away from pro-fibrotic signaling and engaging a CB1R/β-arrestin-1/Akt inhibitory pathway. In murine models of advanced fibrosis, peripheral CB1R blockade by JD5037 successfully attenuates structural renal damage and drastically reduces pro-inflammatory cytokine expression without inducing any behavioral markers of psychiatric distress.

An alternative, and potentially safer, approach to avoid the psychiatric liabilities associated with inverse agonism is the deployment of neutral antagonists. Inverse agonists actively suppress the constitutive, basal activity of the receptor, which in the central nervous system can precipitate severe mood disorders; neutral antagonists, however, merely block endogenous ligand binding without suppressing the receptor's baseline tone.

From a phytocannabinoid perspective, Δ9-tetrahydrocannabivarin (THCV) offers an exceptionally unique pharmacological profile in this regard. Structurally homologous to the intoxicating Δ9-THC, THCV possesses a 3-carbon propyl chain rather than a 5-carbon pentyl chain. This minor structural deviation profoundly alters its binding kinetics. THCV acts as a potent, neutral CB1R antagonist at low and moderate doses, with a reported binding affinity (Ki) ranging between 22 and 75 nM. High-resolution structural studies utilizing crystal structures of the CB1 receptor (e.g., PDB: 5XRA) reveal that the agonist activity of cannabinoids is strongly correlated with their ability to occupy the main hydrophobic pocket (M-pocket) and force open a specific "toggle switch" defined by the residues Phe200 and Trp356. The shorter propyl chain of THCV allows it to occupy the orthosteric site, specifically engaging side pocket 1, without triggering this critical toggle switch, thus locking the receptor in an inactive conformation without exerting inverse agonism. In vivo, THCV has demonstrated significant utility in reversing insulin resistance, reducing hepatic steatosis, and modulating metabolic syndrome parameters without inducing psychoactive effects. In the context of ADPKD, THCV represents a compelling, naturally derived scaffold for peripheral CB1R blockade.

## CB2 receptor agonism for inflammation resolution

In direct contrast to the generally deleterious effects of renal CB1R activation, signaling through the CB2R exerts potent anti-inflammatory, immunomodulatory, and anti-fibrotic effects across multiple organ systems. The CB2 receptor is predominantly expressed on immune cells, particularly on the macrophages that orchestrate the intense interstitial inflammation driving cyst expansion and fibrosis in ADPKD.

The targeted activation of CB2R using highly selective synthetic agonists—such as AM1241, JWH-133, and SMM-295—has been shown to fundamentally redirect macrophage polarization. Rather than adopting a tissue-destructive, pro-inflammatory (M1) phenotype, CB2R agonism forces macrophages toward an anti-inflammatory, tissue-resolving (M2) phenotype. In complex models of ischemia-reperfusion injury and acute kidney injury, CB2R agonism actively prevents tubular epithelial cell apoptosis, significantly reduces proteinuria, and preserves basal renal hemodynamics. At the molecular signaling level, CB2R activation directly suppresses the expression of transforming growth factor-β1 (TGF-β1), thereby arresting the fibrogenic response and mitigating the epithelial-to-mesenchymal transition that permanently scars the kidney.

Because the pathophysiology of ADPKD relies on a dual axis of metabolic dysregulation (driven by CB1R) and interstitial inflammation (driven by macrophages), coupling a highly selective CB2R agonist with a peripherally restricted CB1R antagonist presents a synergistic pharmacological strategy in the briefing’s argument. This dual modulation would address both the source of the metabolic reprogramming and the mechanism of the structural scarring simultaneously.

## Atypical receptors, TRP channels, and cannabidiol toxicity

Beyond the classical CB1 and CB2 receptors, the extended endocannabinoid system encompasses several "atypical" targets, most notably the G protein-coupled receptor 55 (GPR55) and various Transient Receptor Potential (TRP) ion channels.

GPR55 is a Gq-coupled receptor expressed throughout the kidney, vascular endothelium, and gastrointestinal tract. Unlike the canonical cannabinoid receptors that typically initiate inhibitory effects via Gi/o proteins, GPR55 generally promotes excitatory pathways, driving intracellular calcium mobilization, RhoA-dependent cell migration, and pro-inflammatory responses. Cannabidiol (CBD), the major non-psychotropic phytocannabinoid, acts as a highly potent antagonist at GPR55. While GPR55 antagonism might theoretically confer anti-inflammatory benefits, extreme caution is warranted regarding the high-dose administration of CBD in renal disease.

Recent toxicological evaluations reveal that prolonged, high-dose exposure to CBD induces severe cytotoxicity in renal podocytes. This toxicity is not mediated through the classical CB1/CB2 pathways, but rather through profound intracellular calcium dysregulation and a subsequent collapse of mitochondrial bioenergetics, leading to irreversible tubular damage and cell death. Consequently, while CBD possesses numerous anti-inflammatory properties in other tissues, its direct application to a structurally failing kidney may accelerate renal decline (briefing claim; not a v1 confirmatory test).

Furthermore, TRP channels, particularly TRPV4 and TRPV1, are integral to mechanosensation, osmoregulation, and nociception within the renal epithelium. ADPKD is inherently linked to disrupted calcium channel physiology due to the underlying polycystin mutations. TRPV4 is widely expressed throughout the renal tubules and is actively modulated by several phytocannabinoids, including CBD and cannabigerol (CBG). Both CBD and CBG interact with these TRP channels, potentially desensitizing them and thereby offering a potent, non-opioid analgesic pathway for the severe flank pain frequently experienced by ADPKD patients. However, because ADPKD is a disease fundamentally driven by defects in ciliary calcium signaling, any pharmacological modulation of calcium-permeable TRP channels must be approached with extreme computational precision to avoid inadvertently exacerbating cystogenesis.

## Endocannabinoid tone restoration via FAAH inhibition

Given the paradoxical depletion of protective endocannabinoids (specifically AEA and 2-AG) in the plasma and tissues of ADPKD patients, inhibiting their enzymatic degradation offers an alternative therapeutic pathway to direct receptor agonism. Fatty acid amide hydrolase (FAAH) is the primary integral membrane enzyme responsible for the hydrolysis and inactivation of AEA.

In preclinical murine models of renal ischemia-reperfusion injury and progressive fibrogenesis, the administration of selective FAAH inhibitors, such as PF-04457845 and URB597, successfully restored physiological AEA levels. The elevation of AEA tone via FAAH inhibition directly ameliorates increases in blood urea nitrogen and plasma creatinine. Furthermore, FAAH inhibition significantly suppresses TGF-β1-induced profibrogenic markers in primary cultured proximal tubular cells.

Interestingly, recent evidence suggests that the renoprotective effects of FAAH inhibition may be partially mediated by alternative biochemical pathways downstream of AEA, specifically the cyclooxygenase-2 (COX-2) pathway. The breakdown of AEA by COX-2 results in the generation of anti-fibrotic prostamides (such as prostamide E2), indicating that FAAH inhibition protects against fibrogenesis independently of direct CB1R or CB2R activation.

## Pharmacokinetics, drug-drug interactions, and the tolvaptan bottleneck

The integration of any cannabinoid-based therapeutic into the ADPKD clinical paradigm must meticulously account for complex pharmacokinetic interactions, particularly concerning the current standard of care, tolvaptan.

Tolvaptan is extensively metabolized in the liver by the cytochrome P450 3A4 (CYP3A4) enzyme system. CBD, frequently used by patients for pain and anxiety management, is a well-documented, highly potent inhibitor of both CYP3A4 and CYP2C19. The co-administration of CBD with tolvaptan poses an exceptionally severe risk of a pharmacokinetic drug-drug interaction (DDI). By inhibiting CYP3A4, CBD drastically elevates the serum concentration of tolvaptan and its circulating metabolites. Because tolvaptan already carries a significant, FDA-black-box warning for hepatotoxicity, artificially inflating its plasma concentration via CYP3A4 inhibition drastically compounds the risk of acute liver failure. This metabolic overlap fundamentally restricts the concurrent use of high-dose CBD, or any other cannabinoid that heavily inhibits CYP3A4, in patients actively undergoing tolvaptan therapy.

### Table 2. Pharmacokinetic interactions and toxicological risks (briefing)

| Compound | Target | Metabolic pathway / risk | Clinical implication for ADPKD (briefing) |
|---|---|---|---|
| Tolvaptan | V2R (antagonist) | Metabolized heavily by CYP3A4. Induces hepatotoxicity. | Efficacious for cAMP reduction but restricts polypharmacy due to liver risks. |
| Cannabidiol (CBD) | GPR55 (antagonist), TRP | Strong CYP3A4 inhibitor. Podocyte cytotoxicity at high doses (briefing). | Contraindicated with tolvaptan in this narrative; not a v1 claim. |
| Synthetic cannabinoids | CB1R / CB2R (full agonist) | Massive oxidative stress and acute tubular necrosis. | Nephrotoxic; danger of full CB1R agonism in the kidney. |
| Mambaquaretin-1 (MQ1) | V2R (antagonist) | Eliminated via renal reservoirs. Bypasses CYP450 metabolism. | Proposed non-hepatotoxic alternative to tolvaptan. |

## Mambaquaretin-1 (MQ1): resolving the V2R toxicity paradigm

If current V2R antagonism (tolvaptan) is inherently toxic to the liver and incompatible with cannabinoid therapies, an alternative V2R blocker is required (briefing) to synthesize these treatments. Mambaquaretin-1 (MQ1), a naturally occurring 57-amino-acid peptide isolated from the venom of the Eastern green mamba (*Dendroaspis angusticeps*), represents a pharmacological candidate in this space.

MQ1 adopts a Kunitz-fold structure, a highly compact peptide conformation conventionally associated with serine protease inhibition (such as aprotinin inhibiting trypsin) or potassium channel blockade. However, MQ1 exhibits absolute selectivity and sub-nanomolar affinity (Ki = 5.02 nM) for the human V2R. It functions as a full, competitive antagonist, selectively interacting with the V2R through its first loop, thereby blocking all three major V2R activation pathways: cAMP production, β-arrestin recruitment, and MAP kinase activation. Comprehensive screening demonstrates that MQ1 has absolutely no activity on the other 155 GPCRs tested, nor does it affect standard ion channels (briefing).

Crucially, in orthologous murine models of ADPKD (such as *pcy* mice treated daily for 99 days), MQ1 treatment yields a purely aquaretic effect. It significantly reduces both the absolute number of renal cysts and the total area of the cysts (by up to 47%). Most importantly, because MQ1 is a peptide, it is eliminated primarily through renal reservoirs rather than undergoing hepatic CYP450 degradation; consequently, it exhibits absolutely no observed hepatotoxicity, tachyphylaxis, or toxic metabolic byproducts in the cited work. MQ1 entirely bypasses the CYP3A4 drug-drug interaction risks associated with cannabinoids and tolvaptan. Therefore, a dual-therapy approach—utilizing a peripheral CB1R antagonist (like THCV) alongside MQ1—represents a theoretically toxicity-sparing pathway to simultaneously target both the cAMP proliferation axis and the metabolic/fibrotic axis in ADPKD. **This repo does not test that combination in v1.**

## AI-assisted computational workflow

The briefing proposed a Science Superpowers methodology (K-Dense-AI) for later docking and multi-omics work: framing, prior-work survey, analysis design, pre-registration, reproducible setup, execution, anomaly investigation, and red-team review. This study **does** use Superpowers for the agent loop (`docs/SUPERPOWERS.md`) and **does not** run DGX virtual screening until a later sealed protocol.

### Table 3. Multi-omics and structural data sources named in the briefing

| Data modality | Identifier / source | Description | Briefing utility |
|---|---|---|---|
| snRNA-seq / snATAC-seq | GSE185948 (GEO) | Adult human ADPKD kidneys with paired chromatin accessibility | *CNR1* / ECS mapping — **v1 kill** |
| Bulk microarray | GSE7869 (GEO) | Human ADPKD cysts versus normal, minimally cystic tissue | Parked (`EXPLORE.md`) |
| Protein structure | PDB: 5XRA | Human CB1R in complex with agonist AM11542 | Pathway B (parked) |
| Protein structure | PDB: 5M4V | Vasopressin V2R in complex with Mambaquaretin-1 | Pathway D (parked) |
| Protein structure | PDB: 6KPF / 6KPG | CB2R (briefing) | Pathway C (parked) |
| Bulk / other | GSE195460 | Diabetic kidney disease comparison | Parked |

## Concrete experimental pathways (briefing)

The briefing named four computational experiments. **Only Pathway A is in the v1 kill.** B–D are not confirmatory in this checkout.

### Pathway A: transcriptomic validation of ECS targets at single-cell resolution (v1)

Ingest GSE185948 (paired snRNA-seq and snATAC-seq from human ADPKD kidneys). Differential expression of the ECS interactome with the central hypothesis that *CNR1* upregulation is restricted to metabolically failing proximal tubule cells. Correlate with glycolysis and TGF-β1 markers as **exploratory** only. snATAC for *CNR1* chromatin is parked.

### Pathway B: in silico optimization of peripheral CB1 neutral antagonists (parked)

Generative THCV / JD5037 analogs, BBB impermeability filters, docking to inactive CB1 (PDB 5XRA), toggle switch Phe200/Trp356. Not laptop-kill; needs a new protocol.

### Pathway C: structure-based design of dual CB1 antagonist / CB2 agonist compounds (parked)

Comparative MD on CB1 vs CB2 (twin vs single toggle; ECL2). Parked.

### Pathway D: polypharmacology, hepatotoxicity modeling, and CYP450 profiling (parked)

GNN ADMET for CYP3A4/CYP2C19; MQ1–V2R (PDB 5M4V) combination theory. Parked.

---

## Key sources (as provided at study opening)

- Green mamba peptide targets type-2 vasopressin receptor against polycystic kidney disease  
  https://www.pnas.org/doi/abs/10.1073/pnas.1620454114  
  PMC: https://pmc.ncbi.nlm.nih.gov/articles/PMC5502595/

- Single nucleus RNA-seq reveals the process from onset to chronic kidney disease in IgA nephropathy (includes analyses of the GSE185948 ADPKD dataset)  
  https://pmc.ncbi.nlm.nih.gov/articles/PMC12216285/  
  Alternative: https://pmc.ncbi.nlm.nih.gov/articles/PMC13104467/

- PDB 5M4V: Structure of Vasopressin V2R in complex with Mambaquaretin-1  
  https://pdbj.org/mine/summary/5m4v  
  Related: https://pmc.ncbi.nlm.nih.gov/articles/PMC6722740/

- Kidney Interactive Transcriptomics Platform (dataset access and context for GSE185948)  
  https://pmc.ncbi.nlm.nih.gov/articles/PMC13158232/
