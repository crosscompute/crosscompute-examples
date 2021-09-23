import json
from os import environ
from os.path import join


# Get folder paths from environment variables
input_folder = environ.get(
    'CROSSCOMPUTE_INPUT_FOLDER', 'tests/integers/input')
output_folder = environ.get(
    'CROSSCOMPUTE_OUTPUT_FOLDER', 'tests/integers/output')


# Load input variables from input folder
variables = json.load(open(join(input_folder, 'variables.json'), 'rt'))


# Perform calculation
c = variables['a'] + variables['b']


# Save output variables to output folder
json.dump({
    'c': c,
}, open(join(output_folder, 'variables.json'), 'wt'))
