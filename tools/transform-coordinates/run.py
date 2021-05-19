import geotable
import json
from geotable.projections import LONGITUDE_LATITUDE_PROJ4
from os.path import join
from sys import argv


if __name__ == '__main__':
    input_folder, output_folder = argv[1:3]
    settings_path = join(input_folder, 'settings.json')
    settings = json.load(open(settings_path, 'rt'))
    table = geotable.load(
        join(input_folder, 'coordinates.csv'),
        source_proj4=settings['source_proj4'],
        target_proj4=settings['target_proj4'])
    table.save_geojson(
        join(output_folder, 'coordinates.geojson'),
        target_proj4=LONGITUDE_LATITUDE_PROJ4)
    table.save_csv(
        join(output_folder, 'coordinates.csv'))
