#!/bin/bash
pip install \
    geotable
python -u run.py \
    "$CROSSCOMPUTE_INPUT_FOLDER" \
    "$CROSSCOMPUTE_OUTPUT_FOLDER" \
    "$CROSSCOMPUTE_LOG_FOLDER" \
    "$CROSSCOMPUTE_DEBUG_FOLDER"
