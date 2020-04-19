FROM python:3.6-slim as base
WORKDIR /chatty
ENV PYTHONPATH "${PYTHONPATH}:/chatty"
ENV PYTHONBUFFERED True
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY ./src .

FROM base as test_base
COPY test-requirements.txt .
RUN pip install -r test-requirements.txt
