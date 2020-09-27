# An Ontology Model for Climate Data Analysis
This repository includes a complete collection of codes required to generate the results and diagrams presented in the paper: 
> published details of the paper
## Folder Description
### An overview of the folder structure
```
paper_ca_ontology
├── csv2rdf_py
│   ├── ca_model.py
│   └── datasets
│       ├── dublinfull.csv
│       └── shanghaifull.csv
└── dataplot
    ├── globalwarming_sh.png
    ├── globalwarming_sh.py
    ├── p_dublin_1_12.csv
    ├── p_shanghai_1_12.csv
    ├── plot_P_sh_dbl.py
    ├── plot_T_sh_dbl.py
    ├── preciptitation.png
    ├── t_dublin_1_12.csv
    ├── t_shanghai_1_12.csv
    └── temperature.png
```
### Details
There are two main coding parts of this work: 1) defining and populating CA ontology, 2) sample climatic analysis.

- The first part is stored in `csv2rdf_py/` which includes the script `ca_model.py` reading the downloaded [NOAA Climate](https://www.ncdc.noaa.gov/cdo-web/) csv tables from `datasets/`  then converting them to the triples in line with CA ontology.

- The other part is stored in `dataplot/` where a group of scripts `*.py` works for using a group of `*.csv` files (obtained by downloading the solutions to the corresponding SPARQL queries from our published Fuseki endpoint) to result the pictures `*.png` presented in our paper. 

**Note:** 'p' or 'P' in file's name represents 'precipitation' and 't' or 'T' means 'temperature'.
 
