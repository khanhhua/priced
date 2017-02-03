FROM python
MAINTAINER khanhhua <giakhanh2487@gmail.com>

RUN apt -y update
RUN apt install -y python3
RUN apt install -y python3-pip
RUN pip install -U pip wheel setuptools tornado
