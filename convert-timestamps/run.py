import csv
import geopy
import requests
import time
from argparse import ArgumentParser
from crosscompute_table import TableType
from dateutil.parser import parse as parse_datetime
from invisibleroads_macros.disk import make_enumerated_folder_for, make_folder
from invisibleroads_macros.log import format_summary
from invisibleroads_macros.table import duplicate_selected_column_names
from os import environ
from os.path import join
from pytz import timezone


def run(
        target_folder, timestamp_table, timestamp_column,
        source_address, target_address, target_strftime):
    target_path = join(target_folder, 'converted_timestamp_table.csv')
    target_tz = get_timezone_from_address(target_address)
    source_tz = get_timezone_from_address(source_address)

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


def get_timezone_from_address(address):
    geocode = geopy.GoogleV3().geocode
    location = geocode(address)
    timezone_url = 'https://maps.googleapis.com/maps/api/timezone/json'
    try:
        google_key = environ['GOOGLE_KEY']
    except KeyError:
        exit(
            'google_key.missing = Please set GOOGLE_KEY '
            'as an environment variable')
    response = requests.get(timezone_url, {
        'location': '%s,%s' % (location.latitude, location.longitude),
        'timestamp': time.time(),
        'key': google_key,
    })
    return timezone(response.json()['timeZoneId'])


if __name__ == '__main__':
    argument_parser = ArgumentParser()
    argument_parser.add_argument(
        '--target_folder', metavar='FOLDER', type=make_folder)
    argument_parser.add_argument(
        '--timestamp_table_path', metavar='PATH', required=True)
    argument_parser.add_argument(
        '--timestamp_column', metavar='COLUMNS', required=True)
    argument_parser.add_argument(
        '--source_address', metavar='ADDRESS', required=True)
    argument_parser.add_argument(
        '--target_address', metavar='ADDRESS', required=True)
    argument_parser.add_argument(
        '--target_strftime', metavar='STRFTIME', default='%H:%M')
    args = argument_parser.parse_args()
    summary = run(
        args.target_folder or make_enumerated_folder_for(__file__),
        TableType.load(args.timestamp_table_path),
        args.timestamp_column,
        args.source_address,
        args.target_address,
        args.target_strftime)
    print(format_summary(summary))
