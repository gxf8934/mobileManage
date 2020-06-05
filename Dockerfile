FROM python:3.7.6-slim-stretch
RUN echo "Asia/Chongqing" > /etc/timezone
RUN unlink /etc/localtime
RUN ln -s /usr/share/zoneinfo/Asia/Chongqing /etc/localtime
RUN sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list
RUN apt-get clean
RUN apt-get update -y
RUN apt-get install gcc -y
RUN apt-get clean
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install virtualenv
RUN mkdir /opt/app
WORKDIR /opt/app
COPY . /opt/app/
RUN virtualenv venv
RUN . venv/bin/activate
COPY requirements.txt /opt/app/
RUN pip install -r /opt/app/requirements.txt -i https://pypi.douban.com/simple
CMD ["pwd"]
CMD ["/bin/bash","run.sh"]
