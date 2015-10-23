from argparse import ArgumentParser
from dateutil.parser import parse as parse_datetime
from invisibleroads_macros.disk import make_enumerated_folder_for, make_folder
from invisibleroads_macros.log import format_nested_dictionary, format_path
from invisibleroads_macros.table import duplicate_selected_columns
from os.path import join
from pandas import Series, read_csv
from pytz import timezone


def run(
        target_folder, timestamp_table, timestamp_column,
        source_timezone, target_timezone, target_strftime):
    target_path = join(target_folder, 'converted_timestamp_table.csv')
    source_tz = timezone(source_timezone)
    target_tz = timezone(target_timezone)
    convert_timestamp = lambda x: source_tz.localize(x).astimezone(target_tz)
    new_columns = duplicate_selected_columns(
        timestamp_table.columns, [timestamp_column])

    def transform_row(row):
        old_timestamp = parse_datetime(row[timestamp_column])
        new_timestamp = convert_timestamp(old_timestamp)
        new_values = list(row) + [new_timestamp.strftime(target_strftime)]
        return Series(new_values, index=new_columns)
    converted_timestamp_table = timestamp_table.apply(transform_row, axis=1)
    converted_timestamp_table.to_csv(target_path, index=False)
    return {
        'converted_timestamp_table_path': target_path,
    }


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
        '--target_strftime', metavar='STRFTIME')
    args = argument_parser.parse_args()
    timestamp_table = read_csv(args.timestamp_table_path)
    summary = run(
        args.target_folder or make_enumerated_folder_for(__file__),
        timestamp_table,
        args.timestamp_column,
        args.source_timezone,
        args.target_timezone,
        args.target_strftime)
    print(format_nested_dictionary(summary, [
        ('_path', format_path),
    ]))
