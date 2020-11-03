CrossCompute Examples
=====================
Here are example automations made using the CrossCompute framework.

    ENV=~/.virtualenvs/crosscompute
    virtualenv $ENV

    source $ENV/bin/activate
    pip install -U crosscompute

    git clone https://github.com/crosscompute/crosscompute-examples
    cd crosscompute-examples/add-numbers

    export CROSSCOMPUTE_TOKEN=YOUR-TOKEN
    crosscompute automations run
