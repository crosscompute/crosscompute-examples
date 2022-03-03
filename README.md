# CrossCompute Examples

Here are example reports, forms, tools, widgets, dashboards made using the CrossCompute Analytics Automation Framework.

- For documentation, please see https://d.crosscompute.com.
- For tutorials, please see https://forum.crosscompute.com.
- For videos, please see https://youtube.com/crosscompute.

## Usage

```
pip install --upgrade \
    crosscompute>=0.9.1.3 \
    crosscompute-views-map>=0.0.2

cd ~/Documents
git clone https://github.com/crosscompute/crosscompute-examples --recursive
cd crosscompute-examples
git submodule init
git submodule update

# Setup packages
find . -name setup.sh -exec bash '{}' ';'

# Configure environment for reports/map-schools
export MAPBOX_TOKEN=YOUR-MAPBOX-TOKEN
# Configure environment for tools/send-emails
export ATTACHMENTS_FOLDER=~/Documents/attachments

crosscompute
```

You can also use our JupyterLab extensions to create your automation.

```bash
pip install --upgrade \
    jupyterlab-crosscompute>=0.2.0.1

jupyter lab
```

[![CrossCompute Extensions for JupyterLab](https://i.ytimg.com/vi_webp/zFuaJG_39r4/maxresdefault.webp)](https://www.youtube.com/watch?v=zFuaJG_39r4)

## Development

```bash
# Setup packages
find . -name setup.sh -exec bash '{}' ';'

# Install pre-commit hooks
pip install pre-commit
pre-commit install
```
