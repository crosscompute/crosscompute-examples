CrossCompute Examples
=====================
Here are example computational apps made with the CrossCompute framework.

    ENV=~/.virtualenvs/crosscompute
    virtualenv $ENV
    source $ENV/bin/activate
    pip install -U crosscompute
    pip install -U crosscompute-integer crosscompute-text crosscompute-table

    git clone https://github.com/crosscompute/crosscompute-examples
    cd crosscompute-examples/add-integers
    crosscompute run
    crosscompute serve
