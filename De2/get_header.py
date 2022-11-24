from urllib.request import urlopen

LINK = 'https://www.google.com/'
response = urlopen(LINK)
print(response.getheaders())