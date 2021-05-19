#!/bin/bash
pip install \
    invisibleroads-macros-geometry \
    pandas \
    shapely
python -u run.py \
    "$CROSSCOMPUTE_INPUT_FOLDER" \
    "$CROSSCOMPUTE_OUTPUT_FOLDER"
