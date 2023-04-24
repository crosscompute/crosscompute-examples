# Map Schools

- [Configuration](automate.yml)
- [Demo]({ ROOT_URI }/a/map-schools)

```bash
git clone https://github.com/crosscompute/crosscompute-examples
cd crosscompute-examples/reports/map-schools
bash setup.sh

export MAPBOX_TOKEN=YOUR-MAPBOX-TOKEN

# Run development server
pip install crosscompute crosscompute-views-map
crosscompute

# Edit in Jupyter Lab
pip install jupyterlab-crosscompute
jupyter lab
```
