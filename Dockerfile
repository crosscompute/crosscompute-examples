FROM python:3.10
RUN \
useradd --create-home --uid 1000 --user-group user
USER user
WORKDIR /home/user/Projects
COPY --chown=user:user . ./
ENV VIRTUAL_ENV="/home/user/.virtualenvs/crosscompute"
ENV PATH="/home/user/.local/bin:$VIRTUAL_ENV/bin:$PATH"
RUN \
python3 -m venv $VIRTUAL_ENV --system-site-packages && \
find . -name setup.sh -exec bash '{}' ';'
CMD ["crosscompute", "--host", "0.0.0.0", "--port", "7000", "--no-browser", "--production"]
