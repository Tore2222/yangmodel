FROM python:3.6.9

WORKDIR /root/yang2cli

RUN mkdir -p /root/.config/pip

COPY build_env/pip.conf /root/.config/pip/.
COPY build_env/sources.list /etc/apt/.
COPY build_env/requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

