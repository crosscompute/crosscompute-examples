import json
from os.path import join
from sys import argv

input_folder = argv[1]
output_folder = argv[2]

input_path = join(input_folder, 'numbers.json')
output_path = join(output_folder, 'sum.json')

value_by_key = json.load(open(input_path, 'rt'))
value_by_key['c'] = value_by_key['a'] + value_by_key['b']
json.dump(value_by_key, open(output_path, 'wt'))
