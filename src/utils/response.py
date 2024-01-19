def Result(code, message, data=None):
    """简化数据响应的代码"""

    # 如果data没有数据，就去除data属性
    if not data:
        data = []
    if not len(data): return {"code": code, "message": message}

    # return {"code": code, "message": message, **data}
    return {"code": code, "message": message, "data": data}
