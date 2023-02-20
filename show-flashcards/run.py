import json
from os import getenv
from pathlib import Path


input_folder = Path(getenv(
    'CROSSCOMPUTE_INPUT_FOLDER', 'batches/standard/input'))
output_folder = Path(getenv(
    'CROSSCOMPUTE_OUTPUT_FOLDER', 'batches/standard/output'))


with (input_folder / 'cards.md').open('rt') as f:
    text = f.read()


cards = []
for card_text in text.split('==='):
    side_texts = [_.strip() for _ in card_text.split('---')]
    cards.append(side_texts)


with (output_folder / 'cards.json').open('wt') as f:
    json.dump(cards, f)
