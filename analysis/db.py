import sys
import pymysql

# 打开数据库连接
db = pymysql.connect("localhost", "root", "123456", "lagou", charset='utf8')

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 查询语句
sql = "select * from job where positionName like '%java开发%' and education like '%本科%' and city like '%成都%';"

try:
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    print(results)
    print(len(results[0]))
    for row in results:
        print(row)
        # sid = row[0]
        # gender = row[1]
        # class_id=row[2]
        # sname=row[3]
        # # 打印结果
        # print("id是:%s,性别:%s,班级编号:%s,姓名:%s" %(sid, gender,class_id,sname ))
    # print(results)
except:
    print("Error: unable to fetch data")

# 关闭数据库连接
db.close()
