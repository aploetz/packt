#!/usr/bin/python
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import sys

hostname=sys.argv[1]
username=sys.argv[2]
password=sys.argv[3]
userid=sys.argv[4]

nodes = []
nodes.append(hostname)
keyspace="packt"

auth = PlainTextAuthProvider(username=username, password=password)
cluster = Cluster(nodes,auth_provider=auth)
session = cluster.connect(keyspace)

strINSERT = """
    INSERT INTO logins_by_user (user_id,login_datetime,origin_ip)
    VALUES (?,dateof(now()),?)
"""
pINSERTStatement = session.prepare(strINSERT);
session.execute(pINSERTStatement,['aploetz','192.168.0.114'])

strSELECT = """
    SELECT * FROM logins_by_user WHERE user_id=? LIMIT 3;
"""
pSELECTStatement = session.prepare(strSELECT);

rows = session.execute(pSELECTStatement,[userid])
print("Data for user %s:" % userid)
for row in rows:
    #only one row in system.local
    print(row[0] + " " +
          str(row[1]) + " " +
          row[2])

#closing Cassandra connection
session.shutdown()
