#!/usr/bin/python
from redis import StrictRedis
import sys

hostname=sys.argv[1]
password=sys.argv[2]

r = StrictRedis(host=hostname,port=6379,password=password,db=0)

def getPacktWelcome():
    #GET value stored in packt:welcome
    print("Displaying current welcome message...")
    value = r.get('packt:welcome')
    print("message = " + str(value))

def setPacktWelcome():
    #SET new value packt:welcome
    print("Writing \"Hello world from Python!\" to Redis...")
    r.set('packt:welcome','Hello world from Python!')

getPacktWelcome()
setPacktWelcome()
getPacktWelcome()


