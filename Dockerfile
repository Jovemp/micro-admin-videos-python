FROM python:3.10.2-slim

RUN apt update && apt install -y --no-install-recommends \
                                  default-jre \
                                  git

RUN useradd -ms /bin/bash python

USER python

WORKDIR /home/python/app

RUN echo 'HISTFILE=//home/python/zsh/.zsh_history' >> ~/.bashrc

ENV PYTHONPATH=${PYTHONPATH}/home/python/app/src
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-arm64

CMD ["tail", "-f", "/dev/null"]