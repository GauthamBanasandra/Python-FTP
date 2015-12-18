import os
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

__author__ = 'gauth_000'


def main():
    authorizer = DummyAuthorizer()
    authorizer.add_user('gautham_b_a', 'abcd1234', '.', perm='elradfmwM')
    authorizer.add_anonymous(os.getcwd())
    handler = FTPHandler
    handler.authorizer = authorizer
    handler.banner = 'greetings'
    address = ('', 2121)
    server = FTPServer(address, handler)
    server.max_cons = 256
    server.max_cons_per_ip = 5
    server.serve_forever()


if __name__ == '__main__':
    main()
