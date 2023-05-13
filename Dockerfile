FROM python:3.8
WORKDIR /
COPY ./requirements.txt /requirements.txt
RUN pip3 install -r /requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
COPY . /
CMD ["gunicorn","app:app","-c","./gunicorn.conf.py"]