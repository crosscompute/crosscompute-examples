# http://stackoverflow.com/questions/16007204/factorizing-a-number-in-python
import json
from math import sqrt
from os.path import join
from sys import argv


input_folder, output_folder = argv[1:]
variables_dictionary = json.load(open(join(input_folder, 'variables.json')))
x = variables_dictionary['x']


minimum_factor = 2
factors = []
while x > 1:
    for i in range(minimum_factor, int(sqrt(x + 0.05)) + 1):
        if x % i == 0:
            x /= i
            minimum_factor = i
            factors.append(i)
            break
    else:
        if x > 1:
            factors.append(x)
            break


with open(join(output_folder, 'factors.csv'), 'wt') as factors_file:
    factors_file.write('\n'.join(['Factor'] + [str(int(_)) for _ in factors]))
json.dump({'unique_factor_count': len(set(factors))}, open(join(
    output_folder, 'variables.json'), 'wt'))
