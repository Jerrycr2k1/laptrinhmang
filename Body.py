import gzip
import urllib.error
import urllib.request

if __name__ == '__main__':
    try:
        req = urllib.request.Request('http://www.vnexpress.net')
        req.add_header('Accept-Encoding', 'gzip')
        res = urllib.request.urlopen(req)

        header = res.getheaders()
        print(header)
        text = gzip.decompress(res.read())  # lấy body
        # print(text)
    except urllib.error.HTTPError as err:
        print(err.code)
