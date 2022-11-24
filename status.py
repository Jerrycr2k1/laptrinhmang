# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 08:46:51 2022

@author: vuphu
"""

from urllib.request import Request
from urllib.request import urlopen
import gzip

if __name__=='__main__':
    r =Request('http://python.org')
    r.add_header('Accept-Language','vi')
    rl = urlopen(r)
    print(r.get_header('User-agent: '))
    print(rl.url)
    print(rl.status)#trang thai
    print(rl.getheaders())  
    print(rl.getheader('Content-Encoding'))
    print(rl.getheader('Content-Type'))
    f,p =rl.getheader('Content-Type').split(";")
    print(p)