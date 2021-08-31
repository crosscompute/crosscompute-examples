import json
import psutil
from os.path import join


def plot(input_folder, output_folder):
    json.dump({
        'ram-usage': psutil.virtual_memory().percent,
    }, open(join(output_folder, 'variables.json'), 'wt'))
