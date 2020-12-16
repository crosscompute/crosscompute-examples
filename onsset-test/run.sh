#!/bin/bash
pip install \
    onsset

jupyter nbconvert run.ipynb --to notebook --execute --stdout
