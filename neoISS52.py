from neo4j.v1 import GraphDatabase, basic_auth
import sys

hostname=sys.argv[1]
username=sys.argv[2]
password=sys.argv[3]

#connect to local Neo4j
driver = GraphDatabase.driver("bolt://" + hostname + ":7687",
    auth=basic_auth(username,password))
session = driver.session()

#CREATE mission Expedition 52
#session.run("CREATE (:Mission {name:{name}});",
#    {"name":"ISS-51/52 (Soyuz)"})

#CREATE FLOWN_ON edges for astronauts (below) to Expedition 52
createRelationship = """MATCH (m:Mission),(a:Astronaut)
    WHERE m.name = 'ISS-51/52 (Soyuz)' AND l.name='Jack D. Fischer'
    CREATE (a)-[:FLEW_ON]->(m);"""
#session.run(createRelationship)

createRelationship = """MATCH (m:Mission),(a:Astronaut)
    WHERE m.name = 'ISS-51/52 (Soyuz)' AND l.name='Peggy A. Whitson'
    CREATE (a)-[:FLEW_ON]->(m);"""
#session.run(createRelationship)

createRelationship = """MATCH (m:Mission),(a:Astronaut)
    WHERE m.name = 'ISS-51/52 (Soyuz)' AND l.name='Randolph J. Bresnik'
    CREATE (a)-[:FLEW_ON]->(m);"""
session.run(createRelationship)

#query the mission and the edges to the Astronauts
queryRelationship = """MATCH (m:Mission)<-[:FLEW_ON]-
    (a:Astronaut {name:'ISS-51/52'}) RETURN m,a;"""
resultSet = session.run(queryRelationship)

for result in resultSet:
      print("%s from %s" % (result["m"]["name"], result["a"]["name"]))

session.close()
