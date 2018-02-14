from argparse import ArgumentParser
from invisibleroads_macros.disk import make_enumerated_folder_for
from invisibleroads_macros.geometry import flip_xy, transform_geometries
from os.path import basename, join
from pandas import read_csv
from shapely import wkt
from shapely.errors import WKTReadingError


def get_wkt_columns(table):
    try:
        row = table.iloc[0]
    except IndexError:
        return []
    wkt_columns = []
    for column in table.columns:
        try:
            wkt.loads(row[column])
        except WKTReadingError:
            pass
        else:
            wkt_columns.append(column)
    return wkt_columns


def flip_geometry_wkts(geometry_wkts):
    geometries = [wkt.loads(x) for x in geometry_wkts]
    geometries = transform_geometries(geometries, flip_xy)
    return [x.wkt for x in geometries]


if __name__ == '__main__':
    p = ArgumentParser()
    p.add_argument('--target_folder', metavar='FOLDER')
    p.add_argument('wkt_table_path')
    args = p.parse_args()

    t = read_csv(args.wkt_table_path)
    for wkt_column in get_wkt_columns(t):
        t[wkt_column] = flip_geometry_wkts(t[wkt_column])

    target_path = join(
        args.target_folder or make_enumerated_folder_for(__file__),
        basename(args.wkt_table_path))
    t.to_csv(target_path, index=False)
    print('wkt_table_path = %s' % target_path)
