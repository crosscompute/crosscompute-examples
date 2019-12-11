#!/bin/bash
pip install \
    pandas==0.25.3
python run.py \
    $CROSSCOMPUTE_INPUT_FOLDER \
    $CROSSCOMPUTE_OUTPUT_FOLDER
