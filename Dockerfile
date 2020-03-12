FROM python:3.8

WORKDIR /opt/project

RUN pip install poetry>=1.0.0 && \
    pip install gunicorn==20

COPY pyproject.toml poetry.lock /opt/project/

# Turn off auto creation of venvs, use system-wide python in docker image
RUN poetry config virtualenvs.create false && \
    poetry install --no-dev

COPY . /opt/project/

CMD ["/opt/project/run-app.sh"]
