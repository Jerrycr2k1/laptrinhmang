import urllib.error
from urllib.request import urlopen


LINK = 'http://www.debian.org'
try:
    response = urlopen(LINK)
    print('status:', response.status)
except urllib.error.HTTPError as e:
    print('status:', e.code)
    print('reason:', e.reason)