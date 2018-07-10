from flask import *
import unittest
from run import *


class Test(unittest.TestCase):         
 def test_connection1(self):  
   with patch('__main__.mysql.connector.connect') as  mock_mysql_connector_connect:
   	object=TestMySQL()
   	object.before_request()

if __name__ == '__main__':
    unittest.main()       