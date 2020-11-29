from decimal import Decimal
from os.path import join
from pandas import read_csv
from sys import argv


input_folder = argv[1]
output_folder = argv[2]


table_path = join(input_folder, 'numbers.csv')
table = read_csv(table_path)
convert_by_column_name = {
    _: Decimal for _ in table.columns if table[_].dtype.name == 'float64'}
table = read_csv(table_path, converters=convert_by_column_name)


unique_column_name = '+'
while unique_column_name in table.columns:
    unique_column_name += '+'
table[unique_column_name] = table.sum(axis=1)
table.to_csv(join(output_folder, 'sums.csv'), index=False)
