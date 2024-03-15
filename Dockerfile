# 设置基础镜像
FROM python:3.10

# 设置工作目录
WORKDIR /thrive

# 将当前目录中所有文件复制到指定目录中
COPY . /thrive

# 构建镜像时做的事情：下载相关依赖
RUN pip3 install -r requirements.txt -i https://mirrors.bfsu.edu.cn/pypi/web/simple/

# 暴露容器端口号
EXPOSE 5000

# 在容器创建成功后做的事情，相当于执行：python3 app.py
CMD ["python3", "app.py"]