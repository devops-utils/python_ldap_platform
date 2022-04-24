```shell
sudo yum install redis
sudo systemctl restart redis
redis-cli

sudo yum install python3-devel
pip3 install chardet -i https://pypi.tuna.tsinghua.edu.cn/simple/

sudo docker run -it --rm python:3.7 bash

sudo docker build -t yiluxiangbei/ldap-admin:20220424 . 
sudo docker run -it yiluxiangbei/ldap-admin:20220424 bash
# 库迁移
python manage.py makemigrations
python manage.py migrate
# 管理用户创建
python manage.py createsuperuser
python3 manage.py runserver 0.0.0.0:8080

sudo docker run -it -d --name ldap-admin yiluxiangbei/ldap-admin:20220424
sudo docker run -it -d -p 8072:8080 --name ldap-admin yiluxiangbei/ldap-admin:20220424
sudo docker stop ldap-admin
sudo docker start ldap-admin
sudo docker cp online.conf ldap-admin:/ldap-admin/online.conf
sudo docker logs -f ldap-admin
sudo docker exec -it ldap-admin bash

mysql -h127.0.0.1 -uroot -p
create database ldap default character set utf8mb4 collate utf8mb4_unicode_ci;
use ldap;
create user 'ldap'@'127.0.0.1' identified by 'ldap123456';
grant all privileges on ldap.* to 'ldap'@'127.0.0.1';
create user 'ldap'@'%' identified by 'ldap123456';
grant all privileges on ldap.* to 'ldap'@'%';
flush privileges;

/ldap-admin/logs/
/ldap-admin/data

http://49.232.6.131:8072/
http://49.232.6.131:8072/users/login
admin
admin

sudo docker stop ldap-admin
sudo docker rm ldap-admin

cd docker
sudo docker-compose up
sudo docker-compose up -d

sudo docker-compose build ldap-admin

sudo docker-compose up ldap-admin
sudo docker-compose up -d ldap-admin
sudo docker-compose stop ldap-admin

sudo docker exec -it ldap-admin-fe bash

sudo docker-compose logs -f

sqlite3 ldap/data/db.sqlite3

sudo docker push yiluxiangbei/ldap-admin:20220424

docker rmi `docker images | grep none | awk '{print $3}'`
```

```shell
organizationalUnit
groupOfUniqueNames

用户对象类
inetOrgPerson
组对象类
groupOfUniqueNames

```

```shell
cat <<EOF > /etc/apt/sources.list
deb http://mirrors.aliyun.com/ubuntu/ trusty main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ trusty-security main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ trusty-updates main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ trusty-proposed main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ trusty-backports main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ trusty main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ trusty-security main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ trusty-updates main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ trusty-proposed main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ trusty-backports main restricted universe multiverse
EOF

cat <<EOF > /etc/apt/sources.list
deb http://mirrors.aliyun.com/ubuntu/ focal main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ focal main restricted universe multiverse

deb http://mirrors.aliyun.com/ubuntu/ focal-security main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ focal-security main restricted universe multiverse

deb http://mirrors.aliyun.com/ubuntu/ focal-updates main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ focal-updates main restricted universe multiverse

# deb http://mirrors.aliyun.com/ubuntu/ focal-proposed main restricted universe multiverse
# deb-src http://mirrors.aliyun.com/ubuntu/ focal-proposed main restricted universe multiverse

deb http://mirrors.aliyun.com/ubuntu/ focal-backports main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ focal-backports main restricted universe multiverse
EOF

apt-key list

gpg --keyserver keyserver.ubuntu.com --recv-keys 40976EAF437D05B5
gpg --keyserver keyserver.ubuntu.com --recv-keys 3B4FE6ACC0B21F32
apt-get update

https://developer.aliyun.com/mirror/ubuntu?spm=a2c6h.13651102.0.0.310d1b11sBNEzg
lsb_release -a

https://datatables.net/download
```

```
deb http://mirrors.aliyun.com/ubuntu/ trusty main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ trusty-security main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ trusty-updates main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ trusty-proposed main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ trusty-backports main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ trusty main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ trusty-security main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ trusty-updates main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ trusty-proposed main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ trusty-backports main restricted universe multiverse
```