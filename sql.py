import imageio.v2 as imageio

import pymssql

# 连接到数据库
conn = pymssql.connect('DIONG', 'cqycqy', '123456', 'appmanager1')

print('连接成功！')

# 创建游标对象
cursor = conn.cursor()

# 要插入的数据
data = [
    ('梵蒂冈', '每一行'),
    ('阿萨德', '阿萨德刚'),
    # 添加更多的数据
]
# 插入数据的SQL语句
insert_sql = "INSERT INTO 分词 (评论内容, 分词情况) VALUES (%s, %s)"

# 执行插入操作
for row in data:
    cursor.execute(insert_sql, row)

# 提交事务
conn.commit()

# 关闭游标和连接
cursor.close()
conn.close()


