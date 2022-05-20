FROM python
COPY . /home/user/code
RUN \
useradd --uid 1000 --user-group user && \
chown -R user:user /home/user
USER user
WORKDIR /home/user/code
ENV VIRTUAL_ENV="/home/user/.virtualenvs/crosscompute"
ENV PATH="/home/user/.local/bin:$VIRTUAL_ENV/bin:$PATH"
RUN \
python3 -m venv $VIRTUAL_ENV --system-site-packages && \
find . -name setup.sh -exec bash '{}' ';'
CMD ["crosscompute", "--host", "0.0.0.0", "--port", "7000", "--no-browser"]
