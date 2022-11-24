# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 09:51:28 2022

@author: vuphu
"""
from ftplib import FTP
if __name__=='__main__':
    ftp = FTP('ftp.ibiblio.org')
    print(ftp.getwelcome())
    ftp.login()
    print("thu muc hien thoi: ",ftp.pwd())
    dirftp=ftp.nlst()
    f = open('file', "w")
    read = ftp.retrlines('RETR '+'README',f.write)
    ftp.quit()
    print("tong so: ",len(dirftp)," file va thu muc")
    for i in sorted(dirftp):
        print(i)

    