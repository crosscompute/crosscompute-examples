virtualenv ~/.virtualenvs/onsset -p $(which python3.8)
source ~/.virtualenvs/onsset/bin/activate
pip install \
    jupyter \
    onsset \
    pandas \
    xlrd==1.2.0
python -c "$(jupyter nbconvert run.ipynb --to script --stdout)"
