from flask import *
import unittest
from run import app

class SimpleServer(gevent.server.StreamServer):

    def handle(self, socket, address):
        socket.sendall('hello and goodbye!')

class Test(unittest.TestCase):      

    def test(self):
        server = SimpleServer(('127.0.0.1', 0))
        server.start()
        client = gevent.socket.create_connection(('127.0.0.1', server.server_port))
        response = client.makefile().read()
        assert response == 'hello and goodbye!'
        server.stop()

if __name__ == '__main__':
    unittest.main()       