from bs4 import BeautifulSoup
from urlparse import urlparse as parse_url
from werkzeug.test import Client
from werkzeug.wrappers import BaseResponse
import sys
import os, inspect
from crosscompute.configurations import get_tool_definition
from crosscompute.scripts.serve import get_app

def test_serve_add_integers():
	TOOL_FOLDER = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
	tool_definition = get_tool_definition(tool_folder=TOOL_FOLDER, tool_name='', default_tool_name='')
	client = Client(get_app(tool_definition), BaseResponse)	
	response = client.post('/tools/1', data=dict(x_integer = 1, y_integer=665))
	assert 303 == response.status_code
	result_url = parse_url(dict(response.headers)['Location']).path
	response = client.get(result_url)
	soup = BeautifulSoup(response.data)
	assert '666' in soup.find('div', id='standard_output_').text.strip()