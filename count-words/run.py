import csv
import re
from argparse import ArgumentParser
from collections import Counter
from invisibleroads_macros.disk import make_enumerated_folder_for, make_folder
from invisibleroads_macros.log import format_summary
from os.path import join


def run(target_folder, document_text_path):
    text = open(document_text_path, 'rt').read()
    words = re.sub(r'[^a-zA-Z]+', ' ', text).lower().split()
    count_by_word = Counter(words)
    table_path = join(target_folder, 'word_counts.csv')
    csv_writer = csv.writer(open(table_path, 'wt'))
    csv_writer.writerow(['word', 'count'])
    for word, count in sorted(count_by_word.items(), key=lambda x: -x[1]):
        csv_writer.writerow([word, count])
    return {
        'word_count': sum(count_by_word.values()),
        'word_count_table_path': table_path,
    }


if __name__ == '__main__':
    argument_parser = ArgumentParser()
    argument_parser.add_argument(
        '--target_folder', metavar='FOLDER', type=make_folder)
    argument_parser.add_argument(
        '--document_text_path', metavar='PATH', required=True)
    args = argument_parser.parse_args()
    summary = run(
        args.target_folder or make_enumerated_folder_for(__file__),
        args.document_text_path)
    print(format_summary(summary))
