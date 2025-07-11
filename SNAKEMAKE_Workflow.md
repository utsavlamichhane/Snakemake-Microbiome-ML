I am assuming you already have the config.yaml from the SetupEnvironment.md 

So in the activated terminal environment (Python 3.9):

```
configfile: "config.yaml"

rule all:
    input:
        expand(f"{config[\"output_dir\"]/}shap/{{sample}}_shap.png""),
        "results/report.html"

rule dada2:
    conda: "envs/r_env.yaml"
    input:
        fastq_dir=lambda wildcards: config["fastq_dir"]
    output:
        feature_table="{output_dir}/table.tsv",
        taxonomy="{output_dir}/taxonomy.tsv"
    script:
        "scripts/dada2_taxonomy.R"

rule merge:
    conda: "envs/py_env.yaml"
    input:
        table="{output_dir}/table.tsv",
        metadata=config["metadata"]
    output:
        merged="{output_dir}/merged_table.tsv"
    script:
        "scripts/merge_tables.py"

rule train_model:
    conda: "envs/py_env.yaml"
    input:
        data="{output_dir}/merged_table.tsv"
    output:
        model="{output_dir}/model.pkl",
        pca="{output_dir}/pca_components.tsv"
    params:
        model_type=config["model"]["type"],
        params=config["model"]["params"]
    script:
        "scripts/ml_training.py"

rule shap_analysis:
    conda: "envs/py_env.yaml"
    input:
        model="{output_dir}/model.pkl",
        data="{output_dir}/merged_table.tsv"
    output:
        shappng="{output_dir}/shap_summary.png"
    script:
        "scripts/shap_plot.py"

rule report:
    conda: "envs/r_env.yaml"
    input:
        shappng=expand("{output_dir}/shap_summary.png"),
        taxonomy="{output_dir}/taxonomy.tsv"
    output:
        "results/report.html"
    script:
        "report/report.Rmd"
```

I have created a SNAKEFILE in the main branch. Please use that If you dont want to create it manually. 
