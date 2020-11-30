#!/bin/bash
pip install \
    invisibleroads-macros-geometry \
    pandas
python -u run.py \
    "$CROSSCOMPUTE_INPUT_FOLDER" \
    "$CROSSCOMPUTE_OUTPUT_FOLDER"
