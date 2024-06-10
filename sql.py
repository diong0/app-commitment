import imageio.v2 as imageio

import pymssql

# 连接到数据库
conn = pymssql.connect('DIONG', 'cqycqy', '123456', 'appmanager')

print('连接成功！')

import wordcloud

mk = imageio.imread("wujiaoxing.png")

w = wordcloud.WordCloud(width=1000,
                        height=700,
                        background_color='white',
                        font_path='msyh.ttc',
                        mask=mk,
                        scale=15)
w.generate('从明天起')
w.to_file('output1.png')
# 关闭数据库连接
conn.close()
