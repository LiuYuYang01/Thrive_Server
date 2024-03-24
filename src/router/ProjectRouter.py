import psutil
import platform
from datetime import datetime, date

from flask import Blueprint, request

from src.model.ProjectModel import ProjectModel
from src.model.LayoutModel import LayoutModel
from src.utils.response import Result

from src import siwa

# 创建蓝图
project = Blueprint("project", __name__)

from src.siwadoc.ProjectSiwa import ProjectBody


# 获取系统配置
@project.route("/project/system", methods=["GET"])
@siwa.doc(tags=["全局配置"], summary="获取系统配置", description="获取系统配置：CPU、磁盘、IP、系统等等")
def getSystem():
    # 获取CPU信息
    cpu = psutil.cpu_percent(interval=1, percpu=True)
    cpu = round(sum(cpu) / len(cpu), 2)

    # 获取磁盘信息
    disk = psutil.disk_usage('/')
    diskTotal = round(disk.total / 1_073_741_824)  # 总容量
    diskUsed = round(disk.used / 1_073_741_824)  # 已使用容量
    diskFree = round(disk.free / 1073741824)  # 可用容量
    diskPercent = disk.percent  # 已用容量百分比

    # 获取内存信息
    memory = psutil.virtual_memory()
    memoryTotal = round(memory.total / 1_073_741_824, 2)  # 获取内存总量
    memoryAvailable = round(memory.available / 1_073_741_824, 2)  # 获取可用内存
    memoryPercent = memory.percent  # 获取内存已使用百分比
    memoryUsed = round(memory.used / 1_073_741_824, 2)  # 获取已使用内存

    # 系统开机时间
    boot_time = psutil.boot_time()
    boot_time_datetime = datetime.fromtimestamp(boot_time)

    # 获取系统不间断运行天数
    date1 = date(boot_time_datetime.year, boot_time_datetime.month, boot_time_datetime.day)  # 系统开机时间
    date2 = date(datetime.now().year, datetime.now().month, datetime.now().day)
    # 计算日期差
    delta = date2 - date1
    # 获取天数差
    days = delta.days

    # 操作系统信息
    name = platform.system()  # 名称
    version = platform.release()  # 版本

    # 获取系统IP地址
    ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)

    data = {
        "cpu": cpu,
        "disk": {"diskTotal": diskTotal, "diskUsed": diskUsed, "diskFree": diskFree, "diskPercent": diskPercent},
        "memory": {"memoryTotal": memoryTotal, "memoryAvailable": memoryAvailable, "memoryPercent": memoryPercent,
                   "memoryUsed": memoryUsed},
        "boot_time_datetime": boot_time_datetime,
        "name": name,
        "run": days,
        "ip": ip
    }

    return Result(200, "获取系统配置成功", data)


# 获取网站配置
@project.route('/project/web', methods=['GET'])
@siwa.doc(tags=["全局配置"], summary="获取网站配置", description="获取网站配置：标题、描述、LOGO、关键词等等")
def getSite():
    p = ProjectModel()

    p.keyword = (",").join(p.keyword)

    data = {
        'title': p.title,
        'subhead': p.subhead,
        'logo': p.logo,
        'description': p.description,
        'keyword': p.keyword
    }

    return Result(200, "获取网站配置成功", data)


# 修改网站配置
@project.route('/project/web', methods=['PATCH'])
@siwa.doc(tags=["全局配置"], summary="修改网站配置", description="修改网站配置：标题、描述、LOGO、关键词等等",
          body=ProjectBody)
def editSite():
    web = request.json

    web["keyword"] = web["keyword"].split(",")

    data = f"""class ProjectModel(object):
        title = "{web['title']}"  # 网站标题
        subhead = "{web['subhead']}"  # 网站副标题
        logo = "{web['logo']}"  # 网站图标
        description = "{web['description']}"  # 网站描述
        keyword = {web['keyword']}  # 网站SEO关键词
    """

    with open("src/model/ProjectModel.py", "w", encoding="utf8") as f:
        f.write(data)

    return Result(200, "修改网站配置成功")


# 获取布局配置
@project.route('/project/layout', methods=['GET'])
@siwa.doc(tags=["全局配置"], summary="获取布局配置", description="获取布局配置：主题、文章列表、侧边栏、打字机等等")
def getLayout():
    l = LayoutModel()

    data = {
        'isArticleLayout': l.isArticleLayout,
        'rightSidebar': l.rightSidebar,
        'swiperImage': l.swiperImage,
        'swiperText': l.swiperText,
    }

    return Result(200, "获取布局配置成功", data)


# 修改布局配置
@project.route('/project/layout', methods=['PATCH'])
@siwa.doc(tags=["全局配置"], summary="修改布局配置", description="修改布局配置：主题、文章列表、侧边栏、打字机等等",
          body=ProjectBody)
def editLayout():
    layout = request.json

    data = f"""class LayoutModel(object):
        isArticleLayout = "{layout['isArticleLayout']}"
        rightSidebar = "{layout['rightSidebar']}"
        swiperImage = "{layout['swiperImage']}"
        swiperText = str({layout['swiperText']})
    """

    with open("src/model/LayoutModel.py", "w", encoding="utf8") as f:
        f.write(data)

    return Result(200, "修改布局配置成功")
