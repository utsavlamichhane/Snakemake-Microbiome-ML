We need to setup conda environment.

# Set up Conda environment

From your terminal (on the base dir of this repo):

```
conda env create -f envs/py_env.yaml 

```
You should have the yaml file inside the envs directory.

Also, create an R env: 

```
conda env create -f envs/r_env.yaml
```

Similarly, you should have the yaml file inside the envs dir.

Easiest way is to pull the entire repo to your local system.

# Now for the Snakemake lets activate the Python env

```
conda activate py_env
pip install snakemake
```

Also, I am directly writing this config file here as most of you were having problem previously. 

```
fastq_dir: "data/fastq/"         
metadata: "data/metadata.tsv"     
output_dir: "results/"
model:
  type: "random_forest"          
  params:
    n_estimators: 100
    max_depth: 10
```
But, I have this file as config.yaml in the main branch too. 



