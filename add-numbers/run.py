from os import makedirs
from os.path import join
from pandas import read_csv
from sys import argv

source_folder = argv[1]
target_folder = argv[2]
makedirs(target_folder)

source_path = join(source_folder, 'numbers.csv')
target_path = join(target_folder, 'sums.csv')

target_table = read_csv(source_path)
target_table['c'] = target_table['a'] + target_table['b']
target_table.to_csv(target_path, index=False)
