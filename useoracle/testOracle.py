import cx_Oracle as oracle
import json

user='xsxk_jwzj'
pwd='xsxk_jwzj'
url='172.16.7.200:1521/ZHFWDB'

def get_result(conn,sql,dicparam):
    cursor=conn.cursor()
    cursor.execute(sql,dicparam)
    row=cursor.fetchall()
    cols=get_sql_metadata(cursor)
    cursor.close()
    #genarate row as dic
    newrow=[]
    for row1 in row:
        dic1={}
        i=0
        for col in row1:
            if col is not None:
                dic1[cols[i][0]]=col
                i=i+1
        newrow.append(dic1)
    return newrow

def get_sql_metadata(cursor):
    cols=[]
    for col in cursor.description:
        cols.append((col[0],col[1],col[2]))
    return cols

db=oracle.connect(user,pwd,url)
sql='select xnxqdm,kch,kxh,xh,bz,czr,czrxm,xkzy,czip from t_xk_xkjg where xnxqdm=:xnxqdm '
dicparam={'xnxqdm':'2017-2018-2'}

def writedb(row):
    f=open(r'd:\a.txt','w')
    for i in row:
        x=str(i)
        y=json.dumps(x,indent=4,ensure_ascii=False,sort_keys=True)
        #f.write(formatjson(y))
        f.write(formatjson(y))
    f.close()
#import sys
#print(sys.getdefaultencoding())
#sys.setdefaultencoding('utf-8')

#format json
def formatjson(data,encode=None):
    if encode==None:
        x=data
    else:
        x=data.decode(encode)
    return json.dumps(x,
            indent=4,
            ensure_ascii=False,
            sort_keys=True)

row=get_result(db,sql,dicparam)
print(row)
writedb(row)




