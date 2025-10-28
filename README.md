# Supplementary Material — Chagas Disease Cost Analysis (Anonymous Repository)

This repository contains anonymized supplementary materials related to an economic evaluation of Chagas Disease (ChD) across Latin American countries.  
All files have been stripped of identifying information and institutional references for anonymized sharing.

---

## Contents

### 1. `google_search.py`
Python script used to automate the retrieval of bibliographic data from **Google Scholar** via the [SerpAPI](https://serpapi.com).  
It performs iterative searches for cost-related studies on Chagas Disease in six Latin American countries (Argentina, Bolivia, Colombia, Venezuela, Mexico, and Peru), parses results, and exports them to Excel files.

**Main features:**
- Modular function `search_google_scholar()` with customizable parameters.  
- Automatic pagination and deduplication.  
- Output consolidated in `results_google.xlsx` with one sheet per country.  
- Requires `serpapi` and `pandas` packages.

**Usage:**
```bash
pip install serpapi pandas
python google_search.py
```

**Expected output:**  
A file named `results_google.xlsx` containing six worksheets, one per country.

---

### 2. `FileS1.xlsx`, `FileS5.xlsx` to `FileS7.xlsx`
Excel workbooks containing supplementary data tables for the study, including:
- Country-specific cost estimates;
- Healthcare utilization parameters;
- Sensitivity analyses and robustness checks.

Each spreadsheet corresponds to supplementary tables referenced in the manuscript.

---

### 3. `FileS2.pkg`
Package file generated during the data processing or model-building steps (binary format).  
It is provided for reproducibility and version control but is not intended for direct editing.

---

### 4. `FileS3.html`
Interactive appendix summarizing supplementary results and figures related to the manuscript *Age-Related Distribution of Chagas Disease Clinical Forms*.  
It includes detailed data visualizations, supplementary tables, and references generated via Quarto.

---

### 5. `FileS4.docx`
Word document with the textual supplement (“Supplementary Information – Cost Parameter Search Strategy”).  
It describes the methodology used to compile country-level data, including search logic, inclusion criteria, and limitations.

---


## Dependencies

To reproduce or inspect the code, install:
```bash
pip install serpapi pandas openpyxl
```

---

## Methodological Summary

The supplementary script automates literature searches to parameterize cost inputs for ChD modeling across Latin America.  
Due to the limited and heterogeneous nature of published studies, most extracted parameters require critical evaluation before inclusion in any analytical framework.  
The pipeline was designed for reproducibility and minimal human intervention, ensuring consistent bibliographic metadata extraction across regions.

---

## Anonymization Notes

- All author names, institutional affiliations, and local file paths have been removed.  
- Internal directories such as `C:/Users/.../Downloads/` have been replaced with relative file references.  
- Only public-domain or automatically generated identifiers remain.

---

## License

This repository is shared for **academic transparency** under a permissive open license.  
Users are free to inspect, reproduce, or adapt the workflow for research or educational purposes, provided that the original study remains anonymous.
