FROM python:3

WORKDIR /usr/src/app

# Copy all files in current directory into Image
COPY --chown=1000:1000 . /usr/src/app

RUN apt-get update && \
    apt-get install -y wget ssh git vim

RUN pip install --no-cache-dir -r requirements.txt

