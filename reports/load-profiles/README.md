# Electricity Load Profiles Example Report

This example report demonstrates the following:

1. How to output tables and images
2. How to output conditional markdown
3. How to add page breaks
4. How to style individual tables
5. How to show page numbers
6. How to render pages in landscape orientation
7. How to separate common code into modules
8. How to debug notebooks

- To download the datasets, please run `Download Load Profiles 20210505.ipynb` first.
- To generate the report, you will need to install [crosscompute-jupyterlab-extensions](https://pypi.org/project/crosscompute-jupyterlab-extensions) from PyPI and obtain a token from [crosscompute.com](https://crosscompute.com).

```bash
# Prepare environment
virtualenv -p $(which python3) ~/.virtualenvs/crosscompute
source ~/.virtualenvs/crosscompute/bin/activate
pip install --upgrade crosscompute-jupyterlab-extensions
cd load-profiles

# Paste environment variables from crosscompute.com
export CROSSCOMPUTE_CLIENT=https://crosscompute.com
export CROSSCOMPUTE_SERVER=https://services.crosscompute.com
export CROSSCOMPUTE_TOKEN=YOUR-TOKEN

# Download datasets
jupyter nbconvert --to notebook --execute experiments/Download\ Load\ Profiles\ 20210505.ipynb

# Start jupyter
jupyter lab

# Open run.ipynb and click the CrossCompute icon to run the entire report
# OR
# Open sections/residential/run.ipynb and click the CrossCompute icon to run a section
# OR
# Open sections/commercial/run.ipynb and click the CrossCompute icon to run a section
```

## How to output tables and images

## How to output conditional markdown

## How to add page breaks

## How to style individual tables

## How to show page numbers

## How to render pages in landscape orientation

## How to separate common code into modules

We have placed common code into `routines.py` and then imported common routines using the following snippet:

```
import sys
if '..' not in sys.path:
    sys.path.append('..')
    
from routines import (
    load_table,
    parse_timestamp)
```

After updating `routines.py`, be sure to restart your kernel in JupyterLab by pressing zero twice in command mode, i.e. ESC 0 0.

## How to debug notebooks
