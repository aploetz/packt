#!/usr/bin/python
from redis import StrictRedis
import sys

if len(sys.argv) < 4:
    print "Please enter a valid hostname, password, and channel."
    exit(len(sys.argv))

hostname=sys.argv[1]
password=sys.argv[2]
channel=sys.argv[3]

r = StrictRedis(host=hostname,port=6379,password=password,db=0)
channels = r.pubsub()
channels.subscribe(channel)

for message in channels.listen():
    if message['data']=='END':
        break

    if message['data']!=1:
        print message['data']

channels.unsubscribe(channel)
print "Unsubscribed"
