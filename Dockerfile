FROM python:3.8

WORKDIR /opt/project

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
ENV PATH="/root/.poetry/bin:$PATH"

COPY pyproject.toml poetry.lock /opt/project/

# Turn off auto creation of venvs, use system-wide python in docker image
RUN poetry config virtualenvs.create false && \
    poetry install --no-dev

COPY . /opt/project/
# we need to install package itself for version resolving
RUN poetry install --no-dev

CMD ["/opt/project/run-app.sh"]
