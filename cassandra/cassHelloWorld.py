#!/usr/bin/python
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

import sys

hostname=sys.argv[1]
username=sys.argv[2]
password=sys.argv[3]

nodes = []
nodes.append(hostname)

auth = PlainTextAuthProvider(username=username, password=password)
cluster = Cluster(nodes,auth_provider=auth)
session = cluster.connect("system")

#broadcast_address | cluster_name | data_center | listen_address | release_version | rpc_address

strCQL = """
    SELECT cluster_name,data_center,listen_address,release_version
    FROM system.local WHERE key='local';
"""

rows = session.execute(strCQL)
print("Hello world from:")
for row in rows:
    #only one row in system.local
    print(row[0] + " " +
          row[1] + " " +
          row[2] + " " +
          row[3])

#closing Cassandra connection
session.shutdown()
