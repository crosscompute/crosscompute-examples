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
9. How to generate reports over more places

You can see what the reports look like by opening the `examples` subfolder. Here are the steps you can take to recreate those examples.

- To download the datasets, run `Download Load Profiles 20210505.ipynb` first.
- To generate the report, install [crosscompute-jupyterlab-extensions](https://pypi.org/project/crosscompute-jupyterlab-extensions) from PyPI and obtain a token from [crosscompute.com](https://crosscompute.com), then open `run.ipynb` in the root folder and click the CrossCompute icon.

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

Visit [crosscompute.com](https://crosscompute.com) for Training + Support on how to automate your own reports.

## How to output tables and images

1. Save the table with extension `.csv` or image with extension `.png` as a file in the `output_folder` (see `run.ipynb`)
2. Define the output variable with `view: table` or `view: image` (see `tool.yml`)
3. Reference the variable by its id in the template (see `result.md`)

## How to output conditional markdown

1. Save the text with extension `.md` as a file in the `output_folder` (see `run.ipynb`)
2. Define the output variable with `view: markdown` (see `tool.yml`)
3. Reference the variable by its id in the template (see `result.md`)

## How to add page breaks

1. Paste `<div style='page-break-after: always;'></div>` in the template (see `result.md`)

## How to style individual tables

1. Note that each variable id is an HTML class that you can reference in the CSS stylesheet
2. Use a CSS regular expression for efficient pattern matching (see `report.css`)

## How to show page numbers

1. Add `<span class='pageNumber' />` and relevant styles to the footer template (see `footer.md`)
2. Adjust the styles in the footer template to skip page numbering on the first page (see `footer.md`)

## How to render pages in landscape orientation

1. Specify `@page { size: landscape; }` (see `report.css`)
2. Note that if your pages seem to be differently sized from report to report, your tables might be too wide. Try using a larger page size such as `@page { size: legal landscape; }`

## How to separate common code into modules

We have placed common code into `routines.py` and then imported common routines using the following snippet:

```
import sys

def add_modules_folder(folder):
    if folder not in sys.path:
        sys.path.append(folder)

add_modules_folder('../../modules')

from routines import (
    load_table,
    parse_timestamp,
    save_date_plot,
    save_table_description,
    save_table_plot,
    split_table)
```

After updating `routines.py`, be sure to restart your kernel in JupyterLab by pressing zero twice in command mode, i.e. ESC 0 0.

## How to debug notebooks

Thanks to [Xeus Python](https://github.com/jupyter-xeus) team, you can now debug JupyterLab notebooks directly in the browser.

1. Install `xeus-python` using `pip`
2. Select the `XPython` kernel
3. Activate the debugger
4. Set breakpoints
5. Run and step through your code

For command-line scripts and modules such as `routines.py`, we still recommend using `pudb`.

1. Install `pudb` using `pip`
2. Save your notebook to a script `jupyter nbconvert run.ipynb --to script --stdout > run.py`
3. Debug your script `python -m pudb run.py`

##. How to generate reports over more places

1. Replace `names-some.txt` with `names-all.txt` (see `report.yml`)

To speed iteration, we recommend keeping the batch small while prototyping and polishing your report.
