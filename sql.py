import imageio.v2 as imageio

import pymssql


def get_fc():
    # 存储查询结果的列表
    results = []

    # 建立数据库连接
    conn = pymssql.connect(
        server='DIONG',  # SQL Server 地址
        user='cqycqy',  # 用户名
        password='123456',  # 密码
        database='appmanager1'  # 数据库名称
    )

    try:
        # 执行查询
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM 分词")

        # 收集所有行数据
        results = cursor.fetchall()

        # 关闭游标
        cursor.close()
    finally:
        # 关闭数据库连接
        conn.close()

        # 返回查询结果
    return results


def get_pl():
    # 存储查询结果的列表
    results = []

    # 建立数据库连接
    conn = pymssql.connect(
        server='DIONG',  # SQL Server 地址
        user='cqycqy',  # 用户名
        password='123456',  # 密码
        database='appmanager1'  # 数据库名称
    )

    try:
        # 执行查询
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM 评论")

        # 收集所有行数据
        results = cursor.fetchall()

        # 关闭游标
        cursor.close()
    finally:
        # 关闭数据库连接
        conn.close()

        # 返回查询结果
    return results


def get_yh():
    # 存储查询结果的列表
    results = []

    # 建立数据库连接
    conn = pymssql.connect(
        server='DIONG',  # SQL Server 地址
        user='cqycqy',  # 用户名
        password='123456',  # 密码
        database='appmanager1'  # 数据库名称
    )

    try:
        # 执行查询
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM 用户")

        # 收集所有行数据
        results = cursor.fetchall()

        # 关闭游标
        cursor.close()
    finally:
        # 关闭数据库连接
        conn.close()

        # 返回查询结果
    return results


def get_gzapp():
    # 存储查询结果的列表
    results = []

    # 建立数据库连接
    conn = pymssql.connect(
        server='DIONG',  # SQL Server 地址
        user='cqycqy',  # 用户名
        password='123456',  # 密码
        database='appmanager1'  # 数据库名称
    )

    try:
        # 执行查询
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM 用户关注app")

        # 收集所有行数据
        results = cursor.fetchall()

        # 关闭游标
        cursor.close()
    finally:
        # 关闭数据库连接
        conn.close()

        # 返回查询结果
    return results


def getin(comment):
    # 存储查询结果的列表
    results = []

    # 建立数据库连接
    conn = pymssql.connect(
        server='DIONG',  # SQL Server 地址
        user='cqycqy',  # 用户名
        password='123456',  # 密码
        database='appmanager1'  # 数据库名称
    )

    try:
        # 执行查询
        cursor = conn.cursor()
        comment1 = tuple(comment)

        for data in comment1:
            data1 = tuple(data)
            print(data1)
            cursor.execute(
                "INSERT INTO 评论 (评论id, Appid, 评论时间, 应用商店id,App版本号,评论内容,评价) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                data1[:7])

        # 提交事务
        conn.commit()

        # 关闭游标
        cursor.close()
    finally:
        # 关闭数据库连接
        conn.close()

        # 返回查询结果
    return results
