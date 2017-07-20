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
createMission = "CREATE (:Mission {name:{name}});"
session.run(createMission,{"name":"ISS-51/52 (Soyuz)"})

#CREATE FLOWN_ON edges for astronauts (below) to Expedition 52
createRelationship = """MATCH (m:Mission),(a:Astronaut)
    WHERE m.name='ISS-51/52 (Soyuz)' AND a.name='Jack D. Fischer'
    CREATE (a)-[:FLEW_ON]->(m);"""
session.run(createRelationship)

createRelationship = """MATCH (m:Mission),(a:Astronaut)
    WHERE m.name='ISS-51/52 (Soyuz)' AND a.name='Peggy A. Whitson'
    CREATE (a)-[:FLEW_ON]->(m);"""
session.run(createRelationship)

createRelationship = """MATCH (m:Mission),(a:Astronaut)
    WHERE m.name='ISS-51/52 (Soyuz)' AND a.name='Randolph J. Bresnik'
    CREATE (a)-[:FLEW_ON]->(m);"""
session.run(createRelationship)

#query the mission and the edges to the Astronauts
queryRelationship = """MATCH (m:Mission {name:'ISS-51/52 (Soyuz)'})<-[:FLEW_ON]-
    (a:Astronaut) RETURN m,a;"""
resultSet = session.run(queryRelationship)

for result in resultSet:
      print("%s flew on %s" % (result["a"]["name"],result["m"]["name"]))

session.close()
