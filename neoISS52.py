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
session.run("CREATE (:Mission {name:{name}});",
    {"name":"ISS-51/52 (Soyuz)"})

#CREATE FLOWN_ON edges for astronauts (below) to Expedition 52
createRelationship = """MATCH (m:Mission),(a:Astronaut)
    WHERE m.name={mname} AND a.name={aname}
    CREATE (a)-[:FLEW_ON]->(m);"""
session.run(createRelationship,{"mname":"ISS-51/52 (Soyuz)","aname":"Jack D. Fischer"})
session.run(createRelationship,{"mname":"ISS-51/52 (Soyuz)","aname":"Peggy A. Whitson"})
session.run(createRelationship,{"mname":"ISS-51/52 (Soyuz)","aname":"Randolph J. Bresnik"})

#query the mission and the edges to the Astronauts
queryRelationship = """MATCH (m:Mission)<-[:FLEW_ON]-
    (a:Astronaut {name:'ISS-51/52'}) RETURN m,a;"""
resultSet = session.run(queryRelationship)

for result in resultSet:
      print("%s flew on %s" % (result["a"]["name"], result["m"]["name"]))

session.close()
