# An Ontology Model for Climate Data Analysis
This repository includes a complete collection of codes required to generate the results and diagrams presented in the paper: 
> published details of the paper
## Folder Structure
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

`paper_ca_ontology/` Root directory, `csv2rdf_py/` includes the `ca_model.py` file which uses the raw csv data downloaded from [NOAA](https://www.ncdc.noaa.gov/cdo-web/) then stored in `datasets/` to generate the triples in line with CA ontology.

`dataplot/` contains a group of scripts `*.py` that make use of a group of `*.csv` files which are the csv form of the solutions to the queries executed in our Fuseki endpoint to result the pictures `*.png` presented in our paper. **Note:** 'p' or 'P' in file's name represents 'precipitation' and 't' or 'T' means 'temperature'.
 
