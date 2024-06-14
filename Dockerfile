# The Poetry installation is provided through the base image. Please check the
# base image if you interested in the details.
# Base image: https://hub.docker.com/r/pfeiffermax/python-poetry
# Dockerfile: https://github.com/max-pfeiffer/python-poetry/blob/main/build/Dockerfile
ARG BASE_IMAGE
FROM ${BASE_IMAGE}
RUN apt update
RUN apt install -y git

LABEL maintainer="Mike DuPont <jmikedupont2@gmail.com>"

ENV PYTHONUNBUFFERED=1 \
    # https://docs.python.org/3/using/cmdline.html#envvar-PYTHONDONTWRITEBYTECODE
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONPATH=/application_root \
    # https://python-poetry.org/docs/configuration/#virtualenvsin-project
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_CACHE_DIR="/application_root/.cache" \
    VIRTUAL_ENVIRONMENT_PATH="/application_root/.venv" \
    POETRY_HOME="/opt/poetry"
# https://python-poetry.org/docs/#installing-manually 
RUN python -m venv ${VIRTUAL_ENVIRONMENT_PATH} 

# Adding the virtual environment to PATH in order to "activate" it.
# https://docs.python.org/3/library/venv.html#how-venvs-work
ENV PATH="$VIRTUAL_ENVIRONMENT_PATH/bin:$PATH"

# Set the WORKDIR to the application root.
# https://www.uvicorn.org/settings/#development
# https://docs.docker.com/engine/reference/builder/#workdir
WORKDIR ${PYTHONPATH}

# https://python-poetry.org/docs/configuration/#cache-directory
RUN mkdir ${POETRY_CACHE_DIR}

WORKDIR /opt/ai-ticket
COPY pyproject.toml /opt/ai-ticket/
COPY setup.cfg /opt/ai-ticket/
COPY README.md /opt/ai-ticket/
COPY requirements.txt /opt/ai-ticket/
COPY ./src/ /opt/ai-ticket/src/
 
RUN ls ${VIRTUAL_ENVIRONMENT_PATH}/bin/activate
RUN pip install /opt/ai-ticket/ && pip install --trusted-host pypi.python.org -r requirements.txt
