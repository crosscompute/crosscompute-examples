#!/bin/bash
pip install \
    pypdf2 \
    reportlab
python -u run.py \
    "$CROSSCOMPUTE_INPUT_FOLDER" \
    "$CROSSCOMPUTE_OUTPUT_FOLDER"
