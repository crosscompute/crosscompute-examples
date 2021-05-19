#!/bin/bash
pip install \
    pypdf2 \
    PyMuPDF
python -u run.py \
    "$CROSSCOMPUTE_INPUT_FOLDER" \
    "$CROSSCOMPUTE_OUTPUT_FOLDER"
