from ldap3 import Connection,Server
_ldap_ip='127.0.0.1'
_ldap_port='389'
_user='cn=Manager,dc=maxcrc,dc=com'
_passwd='secret'

server=Server(_ldap_ip,port=int(_ldap_port))
conn=Connection(server,user=_user,password=_passwd)
conn.bind()
#test
#conn.extend.standard.who_am_i()
conn.entry

from ldap3 import Server, Connection, ALL
server=Server('127.0.0.1',get_info=ALL)
conn=Connection(server,_user,_passwd,auto_bind=True)
conn.extend.standard.who_am_i()
conn.search('cn=wzp3,ou=mark,dc=maxcrc,dc=com','(objectclass=person)')
t=conn.entries
len(t)

conn.search('cn=wzp3,ou=mark,dc=maxcrc,dc=com','(&(objectclass=person)(uid=a001))')
conn.add('cn=wzp3,ou=mark,dc=maxcrc,dc=com',['person'],{'cn':'wzp3','sn':'a003'})
conn.delete('cn=wzp3,ou=mark,dc=maxcrc,dc=com')
conn.modify('cn=wzp3,ou=mark,dc=maxcrc,dc=com',{'sn':[(MODIFY_REPLACE,['aabb03'])]})
'''
http://www.userbooster.de/en/download/openldap-for-windows.aspx
OpenLDAPforWindows_x86.exe

pip install ldap3

http://ldap3.readthedocs.io/
'''

