import csv
from argparse import ArgumentParser
from crosscompute_table import TableType
from geometryIO import (
    GeometryError, get_spatialReference, get_transformPoint, proj4LL)
from invisibleroads_macros.disk import make_enumerated_folder_for, make_folder
from invisibleroads_macros.log import format_summary, print_error
from os.path import join


COORDINATE_TABLE_UNSUPPORTED_FILE_FORMAT = """\
coordinate_table.error = unsupported file format"""
COORDINATE_COLUMN_NOT_FOUND = """\
coordinate_column_%s.error = "%s" not found"""
COORDINATES_NOT_TRANSFORMED = """
coordinate_table.rows[%s].error = (%s, %s) not transformed"""
SPATIAL_REFERENCE_INVALID = """\
%s_proj4.error = invalid proj4 "%s" """.strip()


def run(
        target_folder, coordinate_table,
        coordinate_column_x, coordinate_column_y,
        source_proj4, target_proj4):
    target_path = join(target_folder, 'converted_coordinate_table.csv')
    try:
        transform_x_y = get_transformPoint(source_proj4, target_proj4)
    except GeometryError:
        try:
            get_spatialReference(source_proj4)
        except GeometryError:
            exit(SPATIAL_REFERENCE_INVALID % ('source', source_proj4))
        try:
            get_spatialReference(target_proj4)
        except GeometryError:
            exit(SPATIAL_REFERENCE_INVALID % ('target', target_proj4))
    columns = list(coordinate_table.columns)
    column_x_index = _get_column_index(columns, coordinate_column_x, 'x')
    column_y_index = _get_column_index(columns, coordinate_column_y, 'y')
    columns, order_x_y = _prepare_columns(columns, target_proj4)

    csv_writer = csv.writer(open(target_path, 'w'))
    csv_writer.writerow(columns)
    for index, row in enumerate(coordinate_table.values):
        row = list(row)
        old_x, old_y = row[column_x_index], row[column_y_index]
        try:
            new_x, new_y = transform_x_y(old_x, old_y)
        except RuntimeError:
            print_error(COORDINATES_NOT_TRANSFORMED, index, old_x, old_y)
            csv_writer.writerow(row + ['', ''])
            continue
        csv_writer.writerow(row + order_x_y(new_x, new_y))
    return [
        ('converted_coordinate_table_path', target_path),
    ]


def _get_column_index(columns, column_name, column_nickname):
    try:
        return columns.index(column_name)
    except ValueError:
        exit(COORDINATE_COLUMN_NOT_FOUND % (column_nickname, column_name))


def _prepare_columns(columns, target_proj4):
    if _normalize_proj4(proj4LL) == _normalize_proj4(target_proj4):
        column_x, column_y = 'Longitude', 'Latitude'
        order_x_y = lambda a, b: [b, a]
    else:
        column_x, column_y = 'X', 'Y'
        order_x_y = lambda a, b: [a, b]
    while column_x in columns or column_y in columns:
        column_x += '*'
        column_y += '*'
    if ''.join(x[:1] for x in columns).islower():
        column_x, column_y = column_x.lower(), column_y.lower()
    return columns + order_x_y(column_x, column_y), order_x_y


def _normalize_proj4(proj4):
    return get_spatialReference(proj4).ExportToProj4()


if __name__ == '__main__':
    argument_parser = ArgumentParser()
    argument_parser.add_argument(
        '--target_folder', metavar='FOLDER', type=make_folder)
    argument_parser.add_argument(
        '--coordinate_table_path', metavar='PATH', required=True)
    argument_parser.add_argument(
        '--coordinate_column_x', metavar='COLUMN', required=True)
    argument_parser.add_argument(
        '--coordinate_column_y', metavar='COLUMN', required=True)
    argument_parser.add_argument(
        '--source_proj4', metavar='PROJ4', required=True)
    argument_parser.add_argument(
        '--target_proj4', metavar='PROJ4', required=True)
    args = argument_parser.parse_args()
    try:
        coordinate_table = TableType().load(args.coordinate_table_path)
    except TypeError:
        exit(COORDINATE_TABLE_UNSUPPORTED_FILE_FORMAT)
    summary = run(
        args.target_folder or make_enumerated_folder_for(__file__),
        coordinate_table,
        args.coordinate_column_x,
        args.coordinate_column_y,
        args.source_proj4,
        args.target_proj4)
    print(format_summary(summary))
