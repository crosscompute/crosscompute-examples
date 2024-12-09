import json
import socket
from pathlib import Path
from sys import argv
from urllib.parse import urlsplit as split_url


input_folder, debug_folder, output_folder = [Path(_) for _ in argv[1:]]
with (input_folder / 'variables.dictionary').open('rt') as f:
    variables = json.load(f)
url = variables['url'].strip()
if url:
    u = split_url(url)
    try:
        packs = socket.getaddrinfo(
            u.hostname or u.path, u.port or u.scheme or 80)
    except socket.gaierror:
        ip_addresses = ['could not query this URL -- please check for typos!']
    else:
        ip_addresses = set(_[4][0] for _ in packs)
else:
    with (debug_folder / 'identities.dictionary').open('rt') as f:
        variables = json.load(f)
    ip_addresses = [variables['ip_address']]
with (output_folder / 'ip-addresses.txt').open('wt') as f:
    f.write('\n\n'.join(sorted(ip_addresses, key=lambda _: (
        ':' in _, len(_), _))))
