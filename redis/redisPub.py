#!/usr/bin/python
from redis import StrictRedis
import sys

print "args=" + str(len(sys.argv))

if len(sys.argv) < 4:
    print "Please enter a valid hostname, password, and channel."
    exit(len(sys.argv))

hostname=sys.argv[1]
password=sys.argv[2]
channel=sys.argv[3]

r = StrictRedis(host=hostname,port=6379,password=password,db=0)
publisher = r.pubsub()

while True:
    message=raw_input("Describe play, or press [Enter] to quit: ")

    if not message:
        break
    else:
        r.publish(channel,message)
        #print message

print "Publish program ended."

