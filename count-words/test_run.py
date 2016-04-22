# coding: utf-8
from crosscompute.tests import run
from string import digits, letters
import re, os, inspect

def test_run_count_words():
    TOOL_FOLDER = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    standard_output = run(
        TOOL_FOLDER, '')[0]
    # check on the result
    assert 'word_count = 113' in standard_output
    # check for the correct target folder (or correct the table path)
    target_folder = re.search(r'\ntarget_folder\s=\s(.+?)\r',standard_output).group(1)
    if '/' in target_folder: 
        check = 'standard_outputs.word_count_table_path = ' + target_folder + '/word_counts.csv'  
    else:    
        check = 'standard_outputs.word_count_table_path = ' + target_folder + '\word_counts.csv'  
    assert check in standard_output