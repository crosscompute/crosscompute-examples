#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from os import getenv, makedirs
input_folder = getenv('CROSSCOMPUTE_INPUT_FOLDER', 'tests/standard/input')
output_folder = getenv('CROSSCOMPUTE_OUTPUT_FOLDER', 'tests/standard/output')
try:
    makedirs(output_folder)
except OSError:
    pass


# In[ ]:


from os.path import join
question_path = join(input_folder, 'question.txt')
question_text = open(question_path, 'rt').read().strip()
question_text


# In[ ]:


import re
normalized_question_text = re.sub(r'\W', ' ', question_text).lower()
normalized_question_terms = normalized_question_text.split()
normalized_question_terms


# In[ ]:


if 'who' in normalized_question_terms:
    response_text = '*you*'
elif 'what' in normalized_question_terms:
    response_text = '*that*'
elif 'where' in normalized_question_terms:
    response_text = '*anywhere*'
else:
    response_text = '?'


# In[ ]:


with open(join(output_folder, 'response.md'), 'wt') as response_file:
    response_file.write(response_text)

