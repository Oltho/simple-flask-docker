FROM python:3.7.13-slim-buster

ENV SERVICE_ACCOUNT_USER=oltho \
    SERVICE_ACCOUNT_GROUP=oltho \
    SERVICE_ACCOUNT_UID=2001 \
    SERVICE_ACCOUNT_GID=2001 \
    PROJECT_NAME=simple_flask_docker \
    FLASK_HOST=0.0.0.0 \
    FLASK_PORT=8080 \
    POETRY_VERSION=1.1.12 \
    PIP_VERSION=22.0.4

# install utils unix package
# hadolint ignore=DL3008
RUN apt-get update && apt-get install --no-install-recommends -y \
  iproute2 \
  && rm -rf /var/lib/apt/lists/*


# creation of service account and directory for project
RUN addgroup --system --gid ${SERVICE_ACCOUNT_GID} ${SERVICE_ACCOUNT_GROUP} \
  && adduser --system --no-create-home --shell /bin/false --uid ${SERVICE_ACCOUNT_UID} --gid ${SERVICE_ACCOUNT_GID} ${SERVICE_ACCOUNT_USER} \
  && mkdir -p /home/${SERVICE_ACCOUNT_USER}/${PROJECT_NAME}

# copy application code
WORKDIR /home/${SERVICE_ACCOUNT_USER}/${PROJECT_NAME}
COPY simple_flask simple_flask
COPY poetry.lock pyproject.toml ./

# Project initialization:
RUN pip install --no-cache-dir --upgrade pip==${PIP_VERSION} \
  && pip install --no-cache-dir poetry==${POETRY_VERSION} \
  && poetry config virtualenvs.create false \
  && poetry install --no-dev --no-interaction --no-ansi

# fix permission
RUN chown -R ${SERVICE_ACCOUNT_USER}:${SERVICE_ACCOUNT_GROUP} /home/${SERVICE_ACCOUNT_USER}/${PROJECT_NAME}
USER ${SERVICE_ACCOUNT_USER}

EXPOSE ${FLASK_PORT}

CMD [ "python", "simple_flask/main.py" ]
