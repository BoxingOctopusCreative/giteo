FROM python:alpine3.9

RUN mkdir -p /src
COPY . /src
WORKDIR /src
RUN python setup.py install
RUN chmod +x /src/entrypoint.sh

ENTRYPOINT ["/src/entrypoint.sh"]