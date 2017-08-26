#!/usr/bin/python
from redis import StrictRedis
from datetime import datetime
import sys

hostname=sys.argv[1]
password=sys.argv[2]
userid=sys.argv[3]
ip=sys.argv[4]

r = StrictRedis(host=hostname,port=6379,password=password,db=0)

def addNewLogin(user,ipaddress):
    print("Logging entry for " + user + " from " + ipaddress)
    time = str(datetime.now())
    r.lpush('packt:logins',user + " " + ipaddress + " " + time)
    r.ltrim('packt:logins',0,2)
    
def getList():
    list = r.lrange('packt:logins',0,-1)
    print(list)

addNewLogin(userid,ip)
getList()


