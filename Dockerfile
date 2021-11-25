FROM python:3.8.9
WORKDIR /doplat
COPY ./ /doplat
RUN /bin/bash -c 'pip install -i https://pypi.tuna.tsinghua.edu.cn/simple importlib-metadata==3.10.1'
RUN /bin/bash -c 'pip install -i https://mirrors.aliyun.com/pypi/simple -r requirements.txt'
ENTRYPOINT ["/doplat/entrypoint.sh"]
