# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 09:38:24 2022

@author: vuphu
"""

from urllib import request
from urllib.request import urlopen
from urllib.request import Request
import urllib.error

#header
if __name__=='__main__':
        header={'Accept-language':'vn'}
        #tao doi tuong request
        req= Request("http://www.vnexpress.net")
        # them header
        req.add_header('Accept-Encoding','gzip')
        #gui request da them option bang urlopen
        response= urlopen(req)
        print(response.getheaders())
        #print(req.header_items())
        #print(response.read())
        #print(response.getheader('Content-Encoding'))
        #data=gzip.decompress(response.read())
        #print(data)
        print(response.getheader('Content-Type'))
