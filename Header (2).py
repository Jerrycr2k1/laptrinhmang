import requests
import json

if __name__=='__main__':
    r=requests.get("http://httpbin.org/get",timeout=5)
    print("Status: "+str(r.status_code))
    print(r.headers)
    if(r.status_code==200):
        results=r.json()
        for i in results.items():
            print(i)
        print("Header")
        for header,value in r.headers.items():
            print(header,'-->',value)
            for header,value in r.request.headers.items():
                print(header,'-->',value)
            print("Server: "+r.headers['server'])
    else:
        print("erro code %s"%r.status_code)
