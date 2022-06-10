FROM python:3.10
RUN useradd user
USER user
WORKDIR /home/user
COPY --chown=user:user . .
ENV VIRTUAL_ENV="/home/user/.virtualenvs/crosscompute"
ENV PATH="/home/user/.local/bin:$VIRTUAL_ENV/bin:$PATH"
RUN \
python -m venv $VIRTUAL_ENV --system-site-packages && \
find . -name setup.sh -exec bash '{}' ';'
CMD ["crosscompute", "--host", "0.0.0.0", "--port", "7000", "--no-browser"]
