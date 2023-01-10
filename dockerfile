FROM nvidia/cuda:11.2.0-cudnn8-runtime-ubuntu18.04

ENV DEBIAN_FRONTEND=noninteractive
ENV DEBCONF_NOWARNINGS=yes
RUN rm /bin/sh && ln -s /bin/bash /bin/sh

RUN apt-get update && apt-get install -y --no-install-recommends \
    sudo curl git wget unzip \
    software-properties-common \
    libgl1-mesa-dev \
    xvfb \
    wkhtmltopdf \
    poppler-utils && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# install node
RUN curl -sL https://deb.nodesource.com/setup_16.x | bash - && \
    apt-get update && apt-get install -y nodejs

# install python3.9
RUN add-apt-repository ppa:deadsnakes/ppa -y
RUN apt-get update && apt install -y python3.9 python3.9-distutils python3.9-venv
RUN ln -s /usr/bin/python3.9 /usr/bin/python
RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && python get-pip.py

RUN mkdir /home/workspace
WORKDIR /home/workspace

RUN git clone https://github.com/discus0434/notion-news.git

# install python packages
RUN cd /home/workspace/notion-news && \
    python -m venv venv && \
    source venv/bin/activate && \
    pip install -r requirements.txt

# install node packages
RUN cd /home/workspace/notion-news && \
    npm install

