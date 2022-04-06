FROM python:3.9

RUN mkdir -p /code/

RUN useradd --create-home --uid 1000 --user-group myapp \
    && chown --recursive myapp:myapp /code

USER myapp
ENV PYTHONUNBUFFERED=1
ENV PATH /home/myapp/.poetry/bin:$PATH
ENV POETRY_PREVIEW=0
WORKDIR /code

RUN curl -sSL https://raw.githubusercontent.com/sdispater/poetry/develop/get-poetry.py | python
RUN poetry config virtualenvs.in-project true

ENTRYPOINT ["/home/myapp/.poetry/bin/poetry", "run"]

# CMD ["jupyter", "lab", "--ip=0.0.0.0"]
CMD ["crosscompute", "--host", "0.0.0.0", "--port", "7000"]

COPY --chown=myapp:myapp . ./

RUN poetry install
