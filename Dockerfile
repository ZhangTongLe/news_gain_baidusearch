FROM  registry.cloud.sinocbd.com/chenby/sinocbd-centos:latest
MAINTAINER zfname <752561131@qq.com>

RUN yum install python34-flask-* python34-pip -y

RUN mkdir -p app
WORKDIR /app/

ADD * /app/


RUN pip3 install -r requirements.txt --upgrade --index-url https://mirrors.aliyun.com/pypi/simple/

EXPOSE 5000

ENTRYPOINT ["python"]
CMD ["Python_Juhe_BaiduSearch.py"]

