import json
from os.path import join
from sys import argv


input_folder, output_folder, log_folder, debug_folder = argv[1:]
value_by_key = json.load(open(join(input_folder, 'numbers.json')))
x = value_by_key['x']


output_dictionary = {}
log_dictionary = {}
debug_dictionary = {}


if x < 10:
    output_dictionary['a'] = 1
    output_dictionary['b'] = 2
    log_dictionary['c'] = 3
    log_dictionary['d'] = 4
    debug_dictionary['e'] = 5
    debug_dictionary['f'] = 6
elif x < 20:
    output_dictionary['a'] = 10
    log_dictionary['c'] = 30
    debug_dictionary['e'] = 50
elif x < 30:
    output_dictionary['a'] = 100
    log_dictionary['c'] = 
elif x < 40:
    output_dictionary['a'] = 1000
    raise Exception('script')
else:
    output_dictionary['a'] = 10000
    raise MemoryError('memory')


json.dump(output_dictionary, open(join(
    output_folder, 'properties.json'), 'wt'))
json.dump(log_dictionary, open(join(
    log_folder, 'properties.json'), 'wt'))
json.dump(log_dictionary, open(join(
    log_folder, 'properties.json'), 'wt'))
json.dump(debug_dictionary, open(join(
    debug_folder, 'properties.json'), 'wt'))
