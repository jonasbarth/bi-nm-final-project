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

The [`2_cross_validation`](2_cross_validation.ipynb) notebook will run a Cross Validation (CV) of these three algorithms
on the `ppi_lcc.txt` and `seed_genes.txt` files, assuming that they are in the project root directory. It will save the 
resulting metrics files in a `metric` folder:

* `metrics/cv_diamond.csv`: precision, recall, and F1 metrics for DIAMonD.
* `metrics/cv_diable.csv`: precision, recall, and F1 metrics for DiaBLE.
* `metrics/cv_diffusion.csv`: precision, recall, and F1 metrics for the Cytoscape Diffusion algorithm.

Additionally, there will be two plots in the `figures` folder:

* `figures/diffusion_comparison.pdf`: precision, recall, and F1 metrics comparison for various `time` parameter values.
* `figures/algorithm_comparison.pdf`: precision, recall, and F1 metrics comparison between DIAMOnD, DiaBLE, and Diffusion.