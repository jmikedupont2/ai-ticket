FROM python:3.10-slim
WORKDIR /opt/ai-ticket
COPY pyproject.toml /opt/ai-ticket/
COPY setup.cfg /opt/ai-ticket/
COPY requirements.txt /opt/ai-ticket/
COPY ./src/ /opt/ai-ticket/src/
RUN pip install /opt/ai-ticket/


RUN apt update
RUN apt install -y git
RUN pip install --trusted-host pypi.python.org -r requirements.txt
