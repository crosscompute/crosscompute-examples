import json
from os.path import join
from sys import argv

input_folder = argv[1]
output_folder = argv[2]

input_path = join(input_folder, 'input.json')
output_path = join(output_folder, 'output-table.json')

value_by_key = json.load(open(input_path, 'rt'))
county_name = value_by_key['county-name']
json.dump(value_by_key, open(output_path, 'wt'))
