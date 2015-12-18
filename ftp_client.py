from ftplib import FTP
__author__ = 'gauth_000'
ftp=FTP('192.168.0.21')
ftp.login(user='gautham_b_a', passwd='abcd1234')
ftp.close()