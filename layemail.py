import urllib.request 
import re
if __name__=='__main__':
    user_agent ='Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36'
    url='https://mmgroup.vn/tao-email-ten-mien-voi-google/'
    opener=urllib.request.build_opener()
    opener.addheaders=[('User-agent',user_agent)]
    urllib.request.install_opener(opener)
    r= urllib.request.urlopen(url)
    data=r.read()
    email =re.compile("[-a-zA-Z0-9._]+[-a-zA-Z0-9._]+@[-a-zA-Z0-9_]+.[a-zA-Z0-9_.]+")
    email_extracted =re.findall(email,str(data))
    print(email_extracted)