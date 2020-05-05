# Extract tables from CORD-19 papers


### Context

This repository contains the scripts used to build a table corpus that was compiled as a contribution to the efforts made to better understand COVID-19. We provide the community with some novel pieces of data that could be valuable. The data provided in the Kaggle challenge can be extended by adding the tables (statistics, experiment summary...etc.) that appear in the scientific articles.

### Content

Over 10.000 covid-19 related scientific articles from [this list](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge#metadata.csv), provided on open access [there](https://www.ncbi.nlm.nih.gov/pmc/), were considered for table extraction. We used [camelot](https://camelot-py.readthedocs.io/en/master/) to attempt an extraction from each paper. Each *.csv* file is a table, the name of the file corresponds to the article title when we can retrieve it. Some files are false postives, they were detected by our extracting script as tables, but they are not.

The licenses for each dataset can be found in this [file](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge#metadata.csv).

Two files are provided: 

- `extract-pdfs.py` scrap the website and save the articles into pdfs.
- `extract-tables-camelot.py` use Camelot lib to extract tables from pdfs.    