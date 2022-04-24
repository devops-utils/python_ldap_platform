FROM python:3.7
RUN cp /etc/apt/sources.list /etc/apt/sources.list.bak
COPY docs/sources.list /etc/apt/sources.list
RUN apt-get update
# RUN sudo apt-get install aptitude -y
# RUN sudo aptitude install python-dev -y
RUN apt-get install python3-dev -y
RUN apt-get install systemd -y

RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
RUN echo 'Asia/Shanghai' > /etc/timezone
WORKDIR /ldap-admin
COPY . .
RUN pip3 install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/
RUN pip3 install six -i https://pypi.tuna.tsinghua.edu.cn/simple/
# 库迁移
# RUN python manage.py makemigrations
# RUN python manage.py migrate
# 管理用户创建
# RUN python manage.py createsuperuser
#CMD ["bash"]
CMD ["tail", "-f", "/dev/null"]
#ENTRYPOINT ["python3", "manage.py", "runserver", "0.0.0.0:8080"]
