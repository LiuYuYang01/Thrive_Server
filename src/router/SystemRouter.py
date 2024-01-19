import psutil
import platform
from datetime import datetime, date

from flask import Blueprint, request

# 创建蓝图
system = Blueprint("system", __name__)

# 导入工具方法
from src.utils.response import Result


# 获取系统配置信息
@system.route("/system/parame", methods=["GET"])
def System():
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

    # 获取系统已不间断运行天数
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
        "name": name + version,
        "run": days,
        "ip": ip
    }

    return Result(200, "获取系统配置信息成功", data)

# # 获取网站配置
# @system.route('/system/web', methods=['GET'])
# def Site():
#     return Result(200, "获取网站配置信息成功")
