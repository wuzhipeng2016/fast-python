'''
about md5 or sha in ldap
'''

import binascii

import os,hashlib,base64
def ldapmd5(data):
    m=hashlib.md5()
    m.update(data.encode())
    return base64.b64encode(m.digest())

def ldapsha(data):
    m=hashlib.sha1()
    m.update(data.encode())
    return base64.b64encode(m.digest())

def ldapssha(data):
    r=os.urandom(4)
    m=hashlib.sha1(data.encode())
    m.update(r)
    return base64.b64encode(m.digest()+r)

def ldapssha(data,key):
    r=key.encode()
    m=hashlib.sha1(data.encode())
    m.update(r)
    print(m.digest()+r)
    br=base64.b64encode(m.digest()+r)
    br2=base64.b64decode(br)
    print(br2)
    return br


#https://my.oschina.net/shawnplaying/blog/733608
def checkpw(challenge_password, password):
    challenge_bytes=base64.b64decode(challenge_password)
    digest = challenge_bytes[:20]
    salt = challenge_bytes[20:]
    hr = hashlib.sha1(password.encode())
    hr.update(salt)
    return digest == hr.digest()

