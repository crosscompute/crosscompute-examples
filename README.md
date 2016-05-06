CrossCompute Examples
=====================
Here are example computational apps made with the CrossCompute framework.

    ENV=~/.virtualenvs/crosscompute
    virtualenv $ENV
    source $ENV/bin/activate
    pip install -U crosscompute
    pip install -U crosscompute-integer
    pip install -U crosscompute-text
    pip install -U crosscompute-table
    pip install -U crosscompute-image
    pip install -U crosscompute-geotable

    git clone https://github.com/crosscompute/crosscompute-examples
    cd crosscompute-examples/add-integers
    crosscompute run
    crosscompute serve
