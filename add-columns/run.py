from os.path import join
from pandas import read_csv
from sys import argv

input_folder = argv[1]
output_folder = argv[2]

input_path = join(input_folder, 'numbers.csv')
output_path = join(output_folder, 'sums.csv')

output_table = read_csv(input_path)
output_table['c'] = output_table['a'] + output_table['b']
output_table.to_csv(output_path, index=False)
