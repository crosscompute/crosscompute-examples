import csv
from argparse import ArgumentParser
from dateutil.parser import parse as parse_datetime
from invisibleroads_macros.disk import make_enumerated_folder_for, make_folder
from invisibleroads_macros.log import format_summary
from invisibleroads_macros.table import duplicate_selected_column_names
from os.path import join
from pandas import read_csv
from pytz import timezone


def run(
        target_folder, timestamp_table, timestamp_column,
        source_timezone, target_timezone, target_strftime):
    target_path = join(target_folder, 'converted_timestamp_table.csv')
    target_tz = timezone(target_timezone)
    source_tz = timezone(source_timezone)

    def convert_timestamp(timestamp):
        return source_tz.localize(timestamp).astimezone(target_tz)

    columns = list(timestamp_table.columns)
    try:
        timestamp_column_index = columns.index(timestamp_column)
    except ValueError:
        exit('%s.error = column not found (%s)' % (
            'timestamp_column', timestamp_column))
    csv_writer = csv.writer(open(target_path, 'w'))
    csv_writer.writerow(duplicate_selected_column_names(
        [timestamp_column], columns))
    for row in timestamp_table.values:
        row = list(row)
        old_timestamp = parse_datetime(row[timestamp_column_index])
        new_timestamp = convert_timestamp(old_timestamp)
        csv_writer.writerow(row + [new_timestamp.strftime(target_strftime)])
    return {'converted_timestamp_table_path': target_path}


if __name__ == '__main__':
    argument_parser = ArgumentParser()
    argument_parser.add_argument(
        '--target_folder', metavar='FOLDER', type=make_folder)
    argument_parser.add_argument(
        '--timestamp_table_path', metavar='PATH', required=True)
    argument_parser.add_argument(
        '--timestamp_column', metavar='COLUMNS', required=True)
    argument_parser.add_argument(
        '--source_timezone', metavar='TIMEZONE', required=True)
    argument_parser.add_argument(
        '--target_timezone', metavar='TIMEZONE', required=True)
    argument_parser.add_argument(
        '--target_strftime', metavar='STRFTIME', default='%H:%M')
    args = argument_parser.parse_args()
    summary = run(
        args.target_folder or make_enumerated_folder_for(__file__),
        read_csv(args.timestamp_table_path),
        args.timestamp_column,
        args.source_timezone,
        args.target_timezone,
        args.target_strftime)
    print(format_summary(summary))
