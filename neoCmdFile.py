from neo4j.v1 import GraphDatabase, basic_auth
import sys

hostname=sys.argv[1]
username=sys.argv[2]
password=sys.argv[3]
filename=sys.argv[4]

commands = []
with open(filename, "r") as infile:
    for line in infile:
        commands.append(line)

#build Cypher command string
astronautCommands = ''.join(commands)

#connect to local Neo4j
driver = GraphDatabase.driver("bolt://" + hostname + ":7687",
    auth=basic_auth(username,password))
session = driver.session()
session.run(astronautCommands)
session.close()

print "Data from " + filename + " loaded!"
