import pymysql
from flask import *

connection = pymysql.connect(host='localhost',user='root',password='',db='flaskdb')
cur = connection.cursor()

def create_tables():
	connection = pymysql.connect(host='localhost',user='root',password='',db='flaskdb')
	with connection.cursor() as cursor:
		cursor.execute("SHOW TABLES LIKE 'users';")
		results=cursor.fetchone()
		if results is not None:
			pass
		else:
		    cursor.execute("CREATE TABLE `admin` (`id` int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,`username` varchar(100) NOT NULL,`password` varchar(100) NOT NULL) ENGINE=InnoDB DEFAULT CHARSET=latin1;")
		    cursor.execute("INSERT INTO `admin`(`AdminID`,`Username`,`Password`)VALUES (1, 'admin','112233');")
		    cursor.execute("CREATE TABLE `comments` (`commentID` int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,`username` varchar(200) NOT NULL,`comment` text NOT NULL,`time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP) ENGINE=InnoDB DEFAULT CHARSET=latin1;")
		    cursor.execute("CREATE TABLE `users` (`userID` int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,`name` varchar(100) NOT NULL,`username` varchar(100) NOT NULL,`email` varchar(100) NOT NULL,`password` varchar(100) NOT NULL,`registration_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP) ENGINE=InnoDB DEFAULT CHARSET=latin1;")
	connection.commit()
	connection.close()