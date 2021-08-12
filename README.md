# 使用docker-compose 部署

上传文件前端静态文件到 /data/yunwei/jfywf

上传后端代码到 /data/yunwei/jsb



启动

```
cd /data/yunwei/jsb
chmod +x entrypoint.sh
docker-compose up -d
```



# 手动部署

#### 前端生产环境部署

提取管理端静态文件

```
python manage.py collectstatic
```

上传文件前端静态文件到 /data/yunwei/jfywf

添加 nginx vhost

```
server {
    listen       80;
    server_name  _;
    charset utf-8;
    client_max_body_size 200m;

    location / {
        root /data/yunwei/jfywf;
    }

    location ^~ /djstatic {
        root /data/yunwei/jsb;
    }

    location ^~ /api {
        proxy_pass    http://127.0.0.1:8000;
        keepalive_timeout  600;
        proxy_read_timeout 600;
        proxy_redirect off;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
    }

    location ^~ /admin {
        proxy_pass    http://127.0.0.1:8000;
        keepalive_timeout  600;
        proxy_read_timeout 600;
        proxy_redirect off;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
    }
}
```



#### 后端生产环境部署

安装包

```
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple importlib-metadata==3.10.1
pip install -i https://mirrors.aliyun.com/pypi/simple -r requirements.txt
```

代码上传到 /data/yunwei/jsb

启动脚本 start.sh

> 启动前设置环境变量
>
> 开发环境: ENV_FILE=jsb/.dev
>
> 生产环境: ENV_FILE=jsb/.prod

```shell
#!/bin/bash
cd /data/yunwei/jsb
export ENV_FILE=jsb/.prod

pip install -i https://pypi.tuna.tsinghua.edu.cn/simple importlib-metadata==3.10.1
pip install -i https://mirrors.aliyun.com/pypi/simple -r requirements.txt

[ -f /var/run/celery/worker.pid ] && rm -f /var/run/celery/worker.pid
celery multi start -A jsb worker -l info -f logs/worker.log
nohup celery -A jsb beat -l info -f logs/beat.log  >/dev/null 2>&1 &
gunicorn jsb.wsgi --bind=0.0.0.0:8000 --log-file logs/INFO.log --workers 8
```

