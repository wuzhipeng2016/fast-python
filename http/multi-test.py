import urllib.request as req
import urllib.parse as parse

url='http://127.0.0.1:5000'

def a():
    for i in range(10000):
        urlnew=url+'/a'+str(i)+'/b'+str(i)
        data=req.urlopen(urlnew).read()
        print(data.decode())

def b():
    url='http://127.0.0.1:5000/testpost'
    for i in range(10):
        data={'a':'aaa'+str(i),'b':'bbbb'+str(i)}
        r=req.Request(url,data=parse.urlencode(data).encode('utf-8'))
        ret=req.urlopen(r).read() 
        print(ret.decode())

b()
