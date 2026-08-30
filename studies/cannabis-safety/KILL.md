# KILL

**Purpose.** Stop overclaiming about cannabis/CBD/CB1 drugs in ADPKD before a counseling-style manuscript. Human-owned pass/fail. Does not mark study 1.

**Named confound.** Two stacked alternatives that would make a single “cannabinoids in ADPKD” headline false:

1. **Collapsed exposure.** Plant cannabis, CBD products, synthetic cannabinoids, and CB1 antagonist drugs are treated as one intervention.
2. **Label laundering.** A theoretical CYP3A4 story is reported as a documented CBD–tolvaptan interaction, ignoring labeled probe data (or the reverse: “no CYP3A4 effect on midazolam” is reported as proof the pair is safe).

## Gate T — taxonomy

**Pass if:** The results table or equivalent has **at least four** rows/sections: (i) plant cannabis, (ii) CBD (OTC vs prescription distinguished if sources allow), (iii) synthetic cannabinoids, (iv) CB1-targeting drugs (antagonist / inverse agonist / antibody as labeled in sources).

**Fail if:** One pooled “cannabinoid” recommendation.

## Gate R — registry emptiness (or honest hits)

**Data:** ClinicalTrials.gov API or equivalent UI export. Frozen query in `PROTOCOL.md`.

**Pass if:** The run records the query string, date, and either **zero** studies meeting the ADPKD + cannabinoid intervention rule, **or** a complete list of hits with NCT IDs (no silent dropping).

**Fail if:** Query not frozen, or hits omitted.

## Gate L — labels

**Pass if:** Jynarque (tolvaptan) and Epidiolex (cannabidiol) labels are cited (DailyMed setids or FDA PI URLs frozen in the unit note). The write-up states: (a) whether each names the other drug; (b) tolvaptan CYP3A / boxed liver warning as on the label; (c) Epidiolex midazolam and P-gp statements as on the label.

**Fail if:** Labels not opened, or briefing text substituted for the label.

## Gate U — unknown DDI

**Pass if:** CBD + tolvaptan is classified **unstudied** unless a dedicated PK/DDI study of that pair is found and cited. Analog bounds (midazolam, everolimus, tacrolimus, grapefruit) may be **narrative** and cannot convert U into “contraindicated” or “safe.”

**Fail if:** Scribe writes contraindicated or safe for the pair without a pair-specific study or a labeled contraindication.

## Decide

| Result | Decision |
|---|---|
| T, R, L, U pass | Complete v1 evidence map; claims ceiling holds |
| T fail | Rewrite; do not Seal a pooled-cannabinoid paper |
| U fail | Not confirmatory; overclaim |
| R or L fail | Incomplete protocol; amend or stop |

## Explicitly not in the kill

GEO *CNR1*. Docking. CYP neural nets. FAERS disproportionality. A 12-person PK trial. Study 1 Gate A/S.
