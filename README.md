# CrossCompute Examples

Here are example reports, forms, tools, widgets, dashboards made using the CrossCompute Analytics Automation Framework.

```
pip install --upgrade \
    crosscompute>=0.9.1 \
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
