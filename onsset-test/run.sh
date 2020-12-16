#!/bin/bash
pip install \
    onsset \
    xlrd==1.2.0

jupyter nbconvert run.ipynb --to notebook --execute --stdout
