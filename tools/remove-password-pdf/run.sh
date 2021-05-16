#!/bin/bash
pip install \
    pypdf2
python -u run.py \
    "$CROSSCOMPUTE_INPUT_FOLDER" \
    "$CROSSCOMPUTE_OUTPUT_FOLDER"
