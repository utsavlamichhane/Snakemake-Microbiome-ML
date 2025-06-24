A Snakemake workflow for end-to-end microbiome machine learning analyses. A beginner-friendly pipeline that:

Starts from raw FASTQ → runs DADA2 & taxonomy assignment (in R).

Extracts feature tables and merges with user metadata.

Performs PCA/PFA and trains a RandomForest or LightGBM model (in Python).

Computes SHAP values and plots feature importance.

Generates an interactive HTML report with R Markdown.
