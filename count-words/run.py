import csv
import json
import re
import sys
from collections import Counter
from os.path import join


input_folder, output_folder = sys.argv[1:]

text_path = join(input_folder, 'text.txt')
text = open(text_path, 'rt').read()
words = re.sub(r'[^a-z]+', ' ', text.lower()).split()
word_counts = sorted(Counter(words).items(), key=lambda _: -_[1])

with open(join(output_folder, 'words.csv'), 'wt') as table_file:
    csv_writer = csv.writer(table_file)
    csv_writer.writerow(['word', 'count'])
    for word, count in word_counts:
        csv_writer.writerow([word, count])

with open(join(output_folder, 'properties.json'), 'wt') as properties_file:
    json.dump({
        'word_count': len(words),
    }, properties_file)
