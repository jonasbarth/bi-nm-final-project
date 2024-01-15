# Bioinformatics and Network Medicine - Final Project
Final Project for Bioinformatics and Network Medicine 2023/2024 at La Sapienza
University, Rome.

This project is about putative disease gene identification and drug repurposing for
Polydactyly, a condition characterised by extra fingers or toes. The project is
organised into 4 parts:

1. PPI and GDA Data Gathering and Processing.
2. Comparative Analysis of Gene Disease Identification Algorithms.
3. Putative Disease Identification.
4. Drug Repurposing.

## Install Requirements
Install the required pip packages in the `requirements.txt` file:
```
pip install -r requirements.txt
```

## Intermediate Files
The project generates several files that can be found at the following locations:

* `data`: contains predicted disease genes and DGIDB results.
* `figures`: figures used in the report.
* `metrics`: contains cross validation metrics.

## 1. PPI and GDA Data Gathering and Processing
The first step of the project is to gather Protein-Protein Interaction (PPI) and
Polydactyly Gene Disease Association (GDA) data. The code for fetching the data,
processing it, describing it, and preparing it for the gene disease identification
algorithms can be found in the [`1_data_gathering`](1_data_gathering.ipynb) notebook.

### Prerequisites
* an internet connection for downloading PPI and GDA data.
* a DisGenet API [token](https://www.disgenet.org/api/#/Authorization) that you place inside an `.env` file in the root directory as
    follows:
    ```
  disgenet_api_token="<api token>"
  ```
* 500MB of free space.

### Output
Running the entire notebook will generate 5 files:
* `ppi_lcc.txt`: an edge list without header for a simple graph containing the Entrez ID of genes of the 
    human interactome.
* `seed_genes.txt`: a list of Entrez IDs of genes associated with Polydactyly and present in the `ppi_lcc.txt` edge list.
* `gda_summary_df.csv`: a summary of the Polydactyly GDA and basic network data.
* `network_metrics.csv`: graph metrics for the disease genes of the disease LCC.
* `betweenness_centrality_csv_degree.pdf`: a scatterplot of node betweenness centrality as a function of node degree.

## 2. Comparative Analysis of Gene Disease Identification Algorithms
Using the `ppi_lcc.txt` and `seed_genes.txt` files, we want to compare three different algorithms in their gene disease
prediction capabilities:

* DIAMOnD
* DiaBLE
* Diffusion

### Requirements
* `ppi_lcc.txt` file from point 1 in the project root folder.
* `seed_genes.txt` file from point 1 in the project root folder.

### Notebook
The [`2_cross_validation`](2_cross_validation.ipynb) notebook will run a Cross Validation (CV) of these three algorithms
on the `ppi_lcc.txt` and `seed_genes.txt` files, assuming that they are in the project root directory. It will save the 
resulting metrics files in a `metric` folder:

* `metrics/cv_diamond.csv`: precision, recall, and F1 metrics for DIAMonD.
* `metrics/cv_diable.csv`: precision, recall, and F1 metrics for DiaBLE.
* `metrics/cv_diffusion.csv`: precision, recall, and F1 metrics for the Cytoscape Diffusion algorithm.

Additionally, there will be two plots in the `figures` folder:

* `figures/diffusion_comparison.pdf`: precision, recall, and F1 metrics comparison for various `time` parameter values.
* `figures/algorithm_comparison.pdf`: precision, recall, and F1 metrics comparison between DIAMOnD, DiaBLE, and Diffusion.

## 3. Putative Disease Identification
To identify new potential disease genes, we run the best algorithm (in our case diffusion) again to predict 100 disease
genes. The notebook [`3_4_putative_disease_gene_identification`](3_4_putative_disease_gene_identification.ipynb) contains
code for running the algorithm and copying the 100 gene symbol identifiers into the clipboard, such that they can be
pasted into the Enrichment Analysis search form.

### Output
The notebook will save the predicted seed genes at:

* `data/putative_disease_genes_entrez.txt`: file with Entrez IDs of putative disease genes. 
* `data/putative_disease_genes_offical_symbols.txt`: file with official symbols of putative disease genes. 

## 4. Drug Repurposing
For the drug repurposing, we want to find approved drugs associated with the predicted disease genes. Again, the notebook 
[`3_4_putative_disease_gene_identification`](3_4_putative_disease_gene_identification.ipynb) contains the code for
copying the 100 predicted genes to the clipboard so that they can be pasted into the 
[dgidb search form](https://old.dgidb.org/search_interactions). 

### Output
The resulting `.tsv` file from the dgidb search can be found at `data/dgidb_approved_drugs.tsv`. 