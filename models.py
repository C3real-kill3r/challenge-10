import pymysql

connection = pymysql.connect(host='localhost',user='root',password='',db='flaskdb',)
cur = connection.cursor()