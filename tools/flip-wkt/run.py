from invisibleroads_macros_geometry import flip_xy, transform_geometries
from os.path import join
from pandas import read_csv
from shapely import wkt
from shapely.errors import WKTReadingError
from sys import argv


def get_wkt_columns(table):
    try:
        row = table.iloc[0]
    except IndexError:
        return []
    wkt_columns = []
    for column in table.columns:
        try:
            wkt.loads(row[column])
        except (AttributeError, UnicodeEncodeError, WKTReadingError):
            pass
        else:
            wkt_columns.append(column)
    return wkt_columns


def flip_geometry_wkts(geometry_wkts):
    geometries = [wkt.loads(x) for x in geometry_wkts]
    geometries = transform_geometries(geometries, flip_xy)
    return [x.wkt for x in geometries]


if __name__ == '__main__':
    input_folder, output_folder = argv[1:3]
    t = read_csv(join(input_folder, 'geometries.csv'))
    for wkt_column in get_wkt_columns(t):
        t[wkt_column] = flip_geometry_wkts(t[wkt_column])
    t.to_csv(join(output_folder, 'geometries.csv'), index=False)
