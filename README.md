# CrossCompute Examples

Here are example reports, forms, tools, widgets, dashboards made using the CrossCompute Analytics Automation Framework.

- For documentation, please see https://docs.crosscompute.com.
- For tutorials, please see https://forum.crosscompute.com.
- For videos, please see https://youtube.com/crosscompute.

## Usage

```bash
cd ~/Projects
git clone https://github.com/crosscompute/crosscompute-examples --recursive
cd crosscompute-examples
git submodule init
git submodule update
```

### Try via Podman

```bash
cd ~/Projects/crosscompute-examples
podman build . -t crosscompute-examples
podman run -it -p 7000:7000 crosscompute-examples
```

If you want to try the examples that require environment variables, use the following commands:

```bash
vim YOUR-ENV-FILE
    MAPBOX_TOKEN=YOUR-MAPBOX-TOKEN
    GOOGLE_KEY=YOUR-GOOGLE-KEY
    ATTACHMENTS_FOLDER=~/Documents/attachments

podman run -it --env-file YOUR-ENV-FILE -p 7000:7000 crosscompute-examples
```

### Try via JupyterLab

```bash
# Setup packages
pip install --upgrade \
    jupyterlab-crosscompute>=0.2.2
find . -name setup.sh -exec bash '{}' ';'

jupyter lab
```

If you want to try the examples that require environment variables, use the following commands:

```bash
pip install --upgrade \
    crosscompute-views-map>=0.1.2
find . -name setup.sh -exec bash '{}' ';'

# Configure environment for reports/map-schools
export MAPBOX_TOKEN=YOUR-MAPBOX-TOKEN
# Configure environment for tools/find-places
export GOOGLE_KEY=YOUR-GOOGLE-KEY
# Configure environment for tools/send-emails
export ATTACHMENTS_FOLDER=~/Documents/attachments

jupyter lab
```

[![CrossCompute Extensions for JupyterLab](https://i.ytimg.com/vi_webp/zFuaJG_39r4/maxresdefault.webp)](https://www.youtube.com/watch?v=zFuaJG_39r4)

### Try via Command Line

```bash
# Setup packages
pip install --upgrade \
    crosscompute>=0.9.2
find . -name setup.sh -exec bash '{}' ';'

crosscompute
```

If you want to try the examples that require environment variables, use the following commands:

```bash
# Setup packages
pip install --upgrade \
    crosscompute-views-map>=0.1.2
find . -name setup.sh -exec bash '{}' ';'

# Configure environment for reports/map-schools
export MAPBOX_TOKEN=YOUR-MAPBOX-TOKEN
# Configure environment for tools/find-places
export GOOGLE_KEY=YOUR-GOOGLE-KEY
# Configure environment for tools/send-emails
export ATTACHMENTS_FOLDER=~/Documents/attachments

crosscompute automate-plus.yml
```

## Development

```bash
# Install pre-commit hooks
pip install pre-commit
pre-commit install
```
