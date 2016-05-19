from crosscompute.tests import run, serve
from pandas import read_csv


def test_add_integers(tmpdir):
    args = str(tmpdir), 'add-integers', {'x_integer': 2, 'y_integer': 3}
    r = run(*args)
    assert r['standard_output'] == '5'
    s = serve(*args)[0]
    assert s.find(id='standard_output-meta').text.strip() == '5'


def test_find_primes(tmpdir):
    args = str(tmpdir), 'find-primes', {'x_integer': 2016}
    r = run(*args)
    assert r['standard_outputs']['unique_factor_count'] == 3


def test_count_words(tmpdir):
    args = str(tmpdir), 'count-words', {'document_text_path': 'words.txt'}
    r = run(*args)
    assert r['standard_outputs']['word_count'] == 113
    t = read_csv(r['standard_outputs']['word_count_table_path'])
    assert t['count'].sum() == 113
    args = str(tmpdir), 'count-words', {
        'document_text-txt': 'curae canitiem inducunt'}
    s = serve(*args)[0]
    s.find(id='word_count-result').text.strip() == '3'
