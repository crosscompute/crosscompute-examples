import csv
import json
from os.path import join
from sys import argv


# Get folder paths from command-line arguments
input_folder, output_folder = argv[1:]


# Load input variables from input folder
rows = []
with open('../locations.csv', 'rt') as f:
    csv_reader = csv.reader(f)
    next(csv_reader)
    for row in csv_reader:
        rows.append([float(_) for _ in row[1:]])
longitudes = [_[0] for _ in rows]
latitudes = [_[1] for _ in rows]


# Save output variables to output folder
json.dump(rows, open(join(output_folder, 'geometries.json'), 'wt'))