FROM python:3.9

# Create the code directory
RUN mkdir -p /code/

# Create a brand new user
RUN useradd --create-home --uid 1000 --user-group myapp \
    && chown --recursive myapp:myapp /code

# The rest of the commands are run as the myapp user, no root here
USER myapp
ENV PYTHONUNBUFFERED=1
ENV PATH /home/myapp/.poetry/bin:$PATH
ENV POETRY_PREVIEW=0
WORKDIR /code

RUN curl -sSL https://raw.githubusercontent.com/sdispater/poetry/develop/get-poetry.py | python
RUN poetry config virtualenvs.in-project true

# By default we want to run within poetry
ENTRYPOINT ["/home/myapp/.poetry/bin/poetry", "run"]

# With the production.ini file, however this can easily be overriden on the command line
# CMD ["jupyter", "lab", "--ip=0.0.0.0"]
CMD ["crosscompute", "--host", "0.0.0.0", "--port", "7000"]
# These steps are last to allow as much caching of the layers as possible

# Copy everything into /code
COPY --chown=myapp:myapp . ./

# Install everything including dependencies, this will install in development
# mode, so if we map the source code over top of what we just copied, we can
# reload automatically
RUN poetry install
