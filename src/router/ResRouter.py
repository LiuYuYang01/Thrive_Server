import os

from flask import Blueprint, request

from src import app
from src.utils.file import randomName
from src.utils.response import Result

from src import siwa


# 创建蓝图
res = Blueprint("res", __name__)

from src.siwadoc.ResSiwa import ResBody

# 文件上传
@res.route("/res", methods=["POST"])
@siwa.doc(tags=["文件管理"], summary="文件上传", description="默认上传到upload目录，可以通过tagger指定文件上传的位置",
          files={'file': {"required": True, "single": False}},
          form=ResBody)
def upload():
    from datetime import datetime
    from werkzeug.utils import secure_filename

    # 获取年、月份
    date = datetime.now()
    year, month = str(date.year), str(date.month)

    # 获取上传的文件对象
    file = request.files['file']

    # 目标存放文件：默认为image
    tagger = request.form.get("tagger", "image", type=str)

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

