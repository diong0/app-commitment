import imageio.v2 as imageio

import pymssql


def get_fc():  # 查询分词
    # 存储查询结果的列表
    results = []

    # 建立数据库连接
    conn = pymssql.connect(
        server='DIONG',  # SQL Server 地址
        user='cqycqy',  # 用户名
        password='123456',  # 密码
        database='appmanager2'  # 数据库名称
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


def get_pl():  # 查询评论
    # 存储查询结果的列表
    results = []

    # 建立数据库连接
    conn = pymssql.connect(
        server='DIONG',  # SQL Server 地址
        user='cqycqy',  # 用户名
        password='123456',  # 密码
        database='appmanager2'  # 数据库名称
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


def get_yh():  # 查询用户
    # 存储查询结果的列表
    results = []

    # 建立数据库连接
    conn = pymssql.connect(
        server='DIONG',  # SQL Server 地址
        user='cqycqy',  # 用户名
        password='123456',  # 密码
        database='appmanager2'  # 数据库名称
    )

    try:
        # 执行查询
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM use_r")

        # 收集所有行数据
        results = cursor.fetchall()

        # 关闭游标
        cursor.close()
    finally:
        # 关闭数据库连接
        conn.close()

        # 返回查询结果
    return results


def get_gzapp():  # 查询用户关注app
    # 存储查询结果的列表
    results = []

    # 建立数据库连接
    conn = pymssql.connect(
        server='DIONG',  # SQL Server 地址
        user='cqycqy',  # 用户名
        password='123456',  # 密码
        database='appmanager2'  # 数据库名称
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


def sign_in(user_id, password, ident):  # 注册
    try:
        # 使用 with 语句自动管理连接资源
        with pymssql.connect(
                server='DIONG',  # SQL Server 地址
                user='cqycqy',  # 用户名
                password='123456',  # 密码
                database='appmanager2'  # 数据库名称
        ) as conn:
            with conn.cursor() as cursor:
                insert_sql = '''  
                    INSERT INTO use_r (用户id, 密码, ident)  
                    VALUES (%s, %s, %s)  
                '''
                cursor.execute(insert_sql, (user_id, password, ident))
                # 提交事务
                conn.commit()
    except pymssql.Error as e:
        print(f"数据库错误: {e}")
    except Exception as e:
        print(f"其他错误: {e}")


def log_in(user_id, password):  # 判断用户登入
    try:
        # 使用 with 语句自动管理连接资源
        with pymssql.connect(
                server='DIONG',  # SQL Server 地址
                user='cqycqy',  # 用户名
                password='123456',  # 密码
                database='appmanager2'  # 数据库名称
        ) as conn:
            with conn.cursor() as cursor:
                # 查询SQL，检查用户ID和密码是否匹配
                query_sql = '''  
                    SELECT ident  
                    FROM use_r  
                    WHERE 用户id=%s AND 密码=%s  
                '''
                cursor.execute(query_sql, (user_id, password))
                result = cursor.fetchall()
    except pymssql.Error as e:
        print(f"数据库错误: {e}")
        result = None
    except Exception as e:
        print(f"其他错误: {e}")
        result = None
    if result:
        return True
    else:
        return False


def view_users(user_id, password):  # 用户界面:显示关注的app
    try:
        # 使用 with 语句自动管理连接资源
        with pymssql.connect(
                server='DIONG',  # SQL Server 地址
                user='cqycqy',  # 用户名
                password='123456',  # 密码
                database='appmanager2'  # 数据库名称
        ) as conn:
            with conn.cursor() as cursor:
                # 查询SQL，检查用户ID和密码是否匹配
                query_sql = '''  
                    select distinct 
                        STUFF(  
                        (SELECT ',' + LTRIM(RTRIM([app名称]))  
                         FROM user_at_a AS ua  
                         JOIN app AS ap ON ua.关注的appid = ap.appid  
                         WHERE ua.用户id = a.用户id AND ua.密码 = a.密码  
                         FOR XML PATH('')), 1, 1, '') AS atappList
                    from user_at_a a,use_r r
                    where r.用户id=a.用户id
                    and	r.密码=a.密码
                    group by a.用户id,a.密码,关注的appid;
                '''
                cursor.execute(query_sql, (user_id, password))
                result = cursor.fetchall()
    except pymssql.Error as e:
        print(f"数据库错误: {e}")
        result = None
    except Exception as e:
        print(f"其他错误: {e}")
        result = None
    return result[0][0]


def at_app(user_id, password, app名称):  # 用户界面:关注某app
    # 输入 用户名 app名
    try:
        # 使用 with 语句自动管理连接资源
        with pymssql.connect(
                server='DIONG',  # SQL Server 地址
                user='cqycqy',  # 用户名
                password='123456',  # 密码
                database='appmanager2'  # 数据库名称
        ) as conn:
            with conn.cursor() as cursor:
                # 查询SQL，检查用户ID和密码是否匹配
                query_sql = '''  
                    insert into user_at_a
                    select %s,%s,Appid
                    from app
                    where [app名称]=%s

                '''
                cursor.execute(query_sql, (user_id, password, app名称))
                conn.commit()
    except pymssql.Error as e:
        print(f"数据库错误: {e}")
    except Exception as e:
        print(f"其他错误: {e}")


def des_app(user_id, password, app_id):  # 用户界面:取关某app
    # 输入 用户名 app名
    try:
        # 使用 with 语句自动管理连接资源
        with pymssql.connect(
                server='DIONG',  # SQL Server 地址
                user='cqycqy',  # 用户名
                password='123456',  # 密码
                database='appmanager2'  # 数据库名称
        ) as conn:
            with conn.cursor() as cursor:
                # 查询SQL，检查用户ID和密码是否匹配
                query_sql = '''  
                    delete user_at_a
                    where [用户id]=%s
                    and[密码]=%s
                    and[关注的appid]=
                    (select appid
                    from app
                    where [app名称]=%s)

                '''
                cursor.execute(query_sql, (user_id, password, app_id))
                conn.commit()
    except pymssql.Error as e:
        print(f"数据库错误: {e}")
    except Exception as e:
        print(f"其他错误: {e}")


def ser_pin(year, month, day, store_name, app_name, score):  # 查询界面:查询某评论内容
    # 输入: 时间 应用商店名 app名 评分
    # 输出 评论内容
    try:
        # 使用 with 语句自动管理连接资源
        with pymssql.connect(
                server='DIONG',  # SQL Server 地址
                user='cqycqy',  # 用户名
                password='123456',  # 密码
                database='appmanager2'  # 数据库名称
        ) as conn:
            with conn.cursor() as cursor:
                # 查询SQL，检查用户ID和密码是否匹配
                query_sql = '''  
                    select 评论内容 
                    from pin
                    where 评论时间=CAST(CAST(%s AS VARCHAR(4)) 
                    + '-' +  RIGHT('0' + CAST(%s AS VARCHAR(2)), 2) 
                    + '-' + RIGHT('0' + CAST(%s AS VARCHAR(2)), 2)
                      AS DATE)
                    and [应用商店id]=
                    (select [应用商店id]
                    from [dbo].[应用商店]
                    where[商店名称]=%s)
                    and[Appid]=(select [Appid]
                    from [dbo].[app]
                    where[app名称]=%s)
                    and [评价]=%s

                '''
                cursor.execute(query_sql, (year, month, day, store_name, app_name, score))
                result = cursor.fetchall()
    except pymssql.Error as e:
        print(f"数据库错误: {e}")
        result = None
    except Exception as e:
        print(f"其他错误: {e}")
        result = None
    return result


# 查询界面:查询某评论内容的分词
# 输入: 评论内容
# 输出 评论内容的分词
def ser_div(pin_c):
    try:
        # 使用 with 语句自动管理连接资源
        with pymssql.connect(
                server='DIONG',  # SQL Server 地址
                user='cqycqy',  # 用户名
                password='123456',  # 密码
                database='appmanager2'  # 数据库名称
        ) as conn:
            with conn.cursor() as cursor:
                # 查询SQL，检查用户ID和密码是否匹配
                query_sql = '''  
                    select [分词情况]
                    from pin_c_d
                    where 评论内容=%s

                '''
                cursor.execute(query_sql, (pin_c))
                result = cursor.fetchall()
    except pymssql.Error as e:
        print(f"数据库错误: {e}")
        result = None
    except Exception as e:
        print(f"其他错误: {e}")
        result = None
    return result


# 查询界面:增加分词
# 输入: 评论内容 增加的分词
def ad_div(pin_c, add_div):
    try:
        # 使用 with 语句自动管理连接资源
        with pymssql.connect(
                server='DIONG',  # SQL Server 地址
                user='cqycqy',  # 用户名
                password='123456',  # 密码
                database='appmanager2'  # 数据库名称
        ) as conn:
            with conn.cursor() as cursor:
                # 查询SQL，检查用户ID和密码是否匹配
                query_sql = '''  
                    insert into [dbo].[pin_c_d]
                    select %s,%s
                    from [dbo].[pin_c_d]
                    where [评论内容]=%s
                    and %s not in
                    (select[分词情况]
                    from[dbo].[pin_c_d]
                    where[评论内容]=%s)

                '''
                cursor.execute(query_sql, (pin_c, add_div, pin_c, add_div, pin_c))
                conn.commit()
    except pymssql.Error as e:
        print(f"数据库错误: {e}")
    except Exception as e:
        print(f"其他错误: {e}")

    # 查询界面:删除分词


# 输入: 评论内容 删除的分词
def de_div(pin_c, add_div):
    try:
        # 使用 with 语句自动管理连接资源
        with pymssql.connect(
                server='DIONG',  # SQL Server 地址
                user='cqycqy',  # 用户名
                password='123456',  # 密码
                database='appmanager2'  # 数据库名称
        ) as conn:
            with conn.cursor() as cursor:
                # 查询SQL，检查用户ID和密码是否匹配
                query_sql = '''  
                    delete [dbo].[pin_c_d]
                    select %s,%s
                    from [dbo].[pin_c_d]
                    where [评论内容]=%s
                    and [分词情况]=%s

                '''
                cursor.execute(query_sql, (pin_c, add_div, pin_c, add_div))
                conn.commit()
    except pymssql.Error as e:
        print(f"数据库错误: {e}")
    except Exception as e:
        print(f"其他错误: {e}")


def change_user(user_id, passwd, atapp, n_user_id, n_passwd, n_atapp):
    try:
        # 使用 with 语句自动管理连接资源
        with pymssql.connect(
                server='DIONG',  # SQL Server 地址
                user='cqycqy',  # 用户名
                password='123456',  # 密码
                database='appmanager2'  # 数据库名称
        ) as conn:
            with conn.cursor() as cursor:
                # 查询SQL，检查用户ID和密码是否匹配
                query_sql = '''  
                    update [dbo].[user_at_a]
                    set [用户id]=%s,
                        [密码]=%s
                        [关注的appid]=%s
                    where [用户id]=%s,
                    and    [密码]=%s
                    and    [关注的appid]=%s

                '''
                cursor.execute(query_sql, (n_user_id, n_passwd, n_atapp, user_id, passwd, atapp))
                conn.commit()
    except pymssql.Error as e:
        print(f"数据库错误: {e}")
    except Exception as e:
        print(f"其他错误: {e}")
def getin(comment):
    # 存储查询结果的列表
    results = []

    # 建立数据库连接
    conn = pymssql.connect(
        server='DIONG',  # SQL Server 地址
        user='cqycqy',  # 用户名
        password='123456',  # 密码
        database='appmanager2'  # 数据库名称
    )

    try:
        # 执行查询
        cursor = conn.cursor()
        comment1 = tuple(comment)

        for data in comment1:
            app_name = data[1]  # Assuming app_name is the second element in the data tuple
            store_name = data[3]  # Assuming store_name is the fourth element in the data tuple

            # 获取 Appid 和 应用商店id
            cursor.execute("SELECT Appid FROM app WHERE app名称 = %s", (app_name,))
            appid_result = cursor.fetchone()
            cursor.execute("SELECT 应用商店id FROM 应用商店 WHERE 商店名称 = %s", (store_name,))
            store_id_result = cursor.fetchone()

            if appid_result and store_id_result:
                appid = appid_result[0]
                store_id = store_id_result[0]
                cursor.execute(
                    "INSERT INTO pin (评论id, Appid, 评论时间, 应用商店id, App版本号, 评论内容, 评价) "
                    "VALUES (%s, %s, %s, %s, %s, %s, %s)",
                    (data[0], appid, data[2], store_id, data[4], data[5], data[6])
                )

        # 提交事务
        conn.commit()

        # 关闭游标
        cursor.close()
    finally:
        # 关闭数据库连接
        conn.close()

    return results
