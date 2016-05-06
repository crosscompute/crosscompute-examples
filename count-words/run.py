import re
import sys
from collections import Counter
from os.path import join
from pandas import Series


target_folder, document_text_path = sys.argv[1:]
target_path = join(target_folder, 'word_counts.csv')
document_text = open(document_text_path, 'rt').read()
words = re.sub(r'[^a-zA-Z]+', ' ', document_text).lower().split()
word_counts = Series(Counter(words))
word_counts.sort_values(ascending=False).to_csv(target_path)


print('word_count = %s' % word_counts.sum())
print('word_count_table_path = %s' % target_path)
