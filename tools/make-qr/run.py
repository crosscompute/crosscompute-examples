import json
from os.path import join
from sys import argv


# Get folder paths from command-line arguments
input_folder, output_folder = argv[1:]


# Load input variables from input folder
variables = json.load(open(join(input_folder, 'variables.dictionary'), 'rt'))


# Perform calculation
c = variables['a'] + variables['b']


# Save output variables to output folder
json.dump({
    'c': c,
}, open(join(output_folder, 'variables.dictionary'), 'wt'))

import qrcode
img = qrcode.make('Some data here')
type(img)  # qrcode.image.pil.PilImage
img.save("some_file.png")
