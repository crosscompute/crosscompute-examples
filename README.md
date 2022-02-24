# CrossCompute Examples

Here are example reports, forms, tools, widgets, dashboards made using the CrossCompute Analytics Automation Framework.

```
pip install --upgrade \
    crosscompute>=0.9.1.1 \
    crosscompute-views-map>=0.0.2

cd ~/Documents
git clone https://github.com/crosscompute/crosscompute-examples --recursive
cd crosscompute-examples
git submodule init
git submodule update
find . -name setup.sh -exec bash '{}' ';'

# Configure environment for reports/map-schools
export MAPBOX_TOKEN=YOUR-MAPBOX-TOKEN
# Configure environment for tools/send-emails
export ATTACHMENTS_FOLDER=~/Documents/attachments

crosscompute
```

You can also use our JupyterLab extensions to create your automation.

```
pip install --upgrade \
    jupyterlab-crosscompute>=0.2.0.1
```

[![CrossCompute Extensions for JupyterLab](https://img.youtube.com/vi/zFuaJG_39r4/0.jpg)](https://www.youtube.com/watch?v=zFuaJG_39r4)

- For documentation, please see https://d.crosscompute.com.
- For tutorials, please see https://forum.crosscompute.com.
- For videos, please see https://youtube.com/crosscompute.
