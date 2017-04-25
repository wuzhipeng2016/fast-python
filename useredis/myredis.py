import redis
import json
import subprocess

#redis config
rconfig={'ip':'127.0.0.1','port':6379,'db':0,'password':'1234567'}

#main function
def getvalue(key):
    if key=='flushdb':
        return flushdb()
    if key=='keys':
        x=getkeys()
        return '\n'.join(x)
    s=key.split(',')
    x=gettype(s[0])
    if x is None:
        return 'key not exists'
    if x=='string':
        d=getstr(key)
        if isjavaobj(d):
            writetotmp(d)
            y=getdatafromtmp()
        elif isjson(d.decode()):
            y=formatjson(d.decode())
        else:
            y=d.decode()
        return y
    if x=='hash':
        if len(s)==1:
            d=gethash(s[0])
            return d
        d=gethash(s[0],s[1])
        return formatjson(d.decode())

#connect redis
def conn():
    r=redis.Redis(host=rconfig['ip'],
            port=rconfig['port'],
            db=rconfig['db'],
            password=rconfig['password'])
    return r

#flushdb
def flushdb():
    r=conn()
    r.flushdb()
    return 'flushdb success'

#get key type
def gettype(key):
    r=conn()
    if r.exists(key):
        return r.type(key).decode()
    return None

#get str value 
def getstr(key):
    r=conn()
    return r.get(key)

#get hash value
def gethash(key,key2=None):
    r=conn()
    if key2 is None:
        return r.hgetall(key)
    return r.hget(key,key2)

#write to file
def writetotmp(data):
    f=open('C:\java2py.dat','wb')
    f.write(data)
    f.close()

#get data from file
def getdatafromtmp():
    p=subprocess.Popen('java -jar java2py.jar',
            stdout=subprocess.PIPE)
    d=p.stdout.read()
    return formatjson(d,'gbk')

#format json
def formatjson(data,encode=None):
    if encode==None:
        x=data
    else:
        x=data.decode(encode)
    return json.dumps(json.loads(x),
            indent=4,
            ensure_ascii=False,
            sort_keys=True)

#keys
def getkeys():
    r=conn()
    keys=r.keys()
    s=set()
    for k in keys:
        sp=k.decode().split('_')
        if sp[0] not in s:
            s.add(sp[0])
    return sorted(s)

#java object serialize start with aced
def isjavaobj(data):
    return data[0]==172 and data[1]==237

def isjson(data):  
    try:  
        json.loads(data)  
    except ValueError:  
        return False  
    return True  
