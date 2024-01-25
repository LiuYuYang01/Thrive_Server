import os

from flask import Blueprint, request

from src import app
from src.utils.file import randomName
from src.utils.response import Result

from src import siwa

# 创建蓝图
res = Blueprint("res", __name__)

from src.siwadoc.ResSiwa import ResBody, PathBody


# 文件上传
@res.route("/file", methods=["POST"])
@siwa.doc(tags=["文件管理"], summary="上传文件", description="默认上传到default目录，可以通过tagger指定文件上传的位置",
          files={'file': {"required": True, "single": False}},
          form=ResBody)
def upload():
    from datetime import datetime
    from werkzeug.utils import secure_filename

    # 获取上传的文件对象
    file = request.files['file']

    # 目标存放文件：默认为image
    tagger = request.form.get("tagger", "default", type=str)

    # 获取年、月份
    date = datetime.now()
    year, month = str(date.year), str(date.month)

    # 项目根目录
    path = app.root_path
    # 获取项目资源存放位置
    upload = app.config["UPLOAD_PATH"]
    uploadPath = path + os.path.join(upload, tagger)

    # 根据年、月份来命名，创建文件目录
    # 判断该目录是否存在, 如果不存在则自动创建
    os.makedirs(uploadPath, exist_ok=True)
    os.makedirs(os.path.join(uploadPath, year), exist_ok=True)
    os.makedirs(os.path.join(uploadPath, year, month), exist_ok=True)
    dirPath = f"{tagger}/{year}/{month}/"

    # 生成唯一文件名
    fileName = secure_filename(randomName(file.filename))

    # 将文件上传到指定的目录
    file.save(os.path.join(uploadPath, year, month, fileName))

    # 拼接文件路径
    url = f"{request.host_url}{dirPath}{fileName}"
    return Result(200, "文件上传成功", url)


# 删除文件
@res.route("/file", methods=["DELETE"])
@siwa.doc(tags=["文件管理"], summary="删除文件", body=PathBody,
          description="根据文件的路径来删除")
def delete():
    path = request.json["path"]

    try:
        os.remove(app.root_path + app.config["UPLOAD_PATH"] + path)
    except FileNotFoundError as e:
        return Result(500, str(e))

    return Result(200, "删除文件成功")


@res.route("/file", methods=["GET"])
@siwa.doc(tags=["文件管理"], summary="获取文件列表")
def list():
    upload = app.config["UPLOAD_PATH"][1:]
    dirs = get_directory_structure(os.path.join(app.root_path, upload))
    return Result(200, "获取文件列表成功", dirs)


def get_directory_structure(path):
    structure = []
    if os.path.isdir(path):
        items = os.listdir(path)

        for item in items:
            item_path = os.path.join(path, item)
            # 如果是文件
            if os.path.isdir(item_path):
                # 如果没有子目录
                if hasDirFile("dir", item_path):
                    children = get_directory_structure(item_path)
                    directory = {
                        "children": children,
                        "list": [],
                        "name": item
                    }
                else:
                    list = get_directory_structure(item_path)
                    directory = {
                        "children": [],
                        "list": list,
                        "name": item
                    }

                structure.append(directory)
            else:
                structure.append(item)
    return structure


# 判断指定目录中有没有目录或文件
def hasDirFile(mark, directory):
    if mark == "dir":
        # 判断当前目录中是否有子目录
        for item in os.listdir(directory):
            if os.path.isdir(os.path.join(directory, item)):
                return True
        return False
    elif mark == "file":
        # 判断当前目录中是否有文件
        for item in os.listdir(directory):
            if os.path.isfile(os.path.join(directory, item)):
                return True
        return False
