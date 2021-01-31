import geotable
import random
from os.path import expanduser, join


FOLDER = expanduser('~/Experiments/lesotho')
source_geotable_path = join(FOLDER, 'lesotho-population-20181001.csv')
target_point_counts = 100, 1000, 10000, 100000, 1000000
print(0)
raw_geotable = geotable.load(source_geotable_path)
print(1)
utm_proj4 = geotable.load_utm_proj4(source_geotable_path)
utm_geotable = geotable.load(source_geotable_path, target_proj4=utm_proj4)
print(2)
random_geometry = random.choice(utm_geotable.geometries)
random_geometry.wkt
print(3)
t = utm_geotable.copy()
column_name = '_distance_in_meters'
t[column_name] = t['geometry_object'].apply(lambda g: g.distance(
    random_geometry))
t = t.sort_values(column_name)
sorted_index = t.index
print(4)
target_folder = FOLDER
for target_point_count in target_point_counts:
    target_index = sorted_index[:target_point_count]
    point_count = len(target_index)

    target_geotable = raw_geotable.loc[target_index]
    target_geotable.save_csv(
        f'{target_folder}/raw-geometries-{point_count}.csv')
    target_geotable.save_shp(
        f'{target_folder}/raw-geometries-{point_count}.shp.zip')

    target_geotable = utm_geotable.loc[target_index]
    target_geotable.save_csv(
        f'{target_folder}/utm-geometries-{point_count}.csv')
    target_geotable.save_shp(
        f'{target_folder}/utm-geometries-{point_count}.shp.zip')

    print(point_count)
