# CrossCompute Examples

Here are example reports, forms, tools, widgets, dashboards made using the CrossCompute Analytics Automation Framework.

```
pip install crosscompute crosscompute-views-map --upgrade

cd ~/Documents
git clone https://github.com/crosscompute/crosscompute-examples --recursive
cd crosscompute-examples
git submodule init
git submodule update
find . -name setup.sh -exec bash '{}' ';'

# Configure environment for reports/map-schools
# export MAPBOX_TOKEN=YOUR-MAPBOX-TOKEN
# Configure environment for tools/send-emails
# export ATTACHMENTS_FOLDER=~/Documents/attachments

crosscompute
```
