import csv
import json
from sys import argv


source_path = argv[1]
target_path = argv[2]


with open(source_path, 'rt') as source_file:
    d = json.load(source_file)
    rows = [(
        _['properties']['NAME'],
        _['geometry']['coordinates'][0],
        _['geometry']['coordinates'][1],
    ) for _ in d['features']]


with open(target_path, 'wt') as target_file:
    csv_writer = csv.writer(target_file)
    csv_writer.writerow(['name', 'longitude', 'latitude'])
    csv_writer.writerows(rows)
