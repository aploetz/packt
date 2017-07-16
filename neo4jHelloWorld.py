from neo4j.v1 import GraphDatabase, basic_auth
import sys

hostname=sys.argv[1]
username=sys.argv[2]
password=sys.argv[3]

#connect to local Neo4j
driver = GraphDatabase.driver("bolt://" + hostname + ":7687",
    auth=basic_auth(username,password))
session = driver.session()

#create Python language entity
session.run("CREATE (:Language {name:{name},version:{ver}});",
    {"name":"Python","ver":"2.7.13"})

#create relationship from Python lanugage to welcome message
createRelationship = """MATCH (m:Message),(l:Language)
    WHERE m.title = 'Welcome' AND l.name='Python'
    CREATE (m)-[:ACCESSED_FROM]->(l);"""
session.run(createRelationship)

#query the message and the relationship to Python
queryRelationship = """MATCH (m:Message)-[:ACCESSED_FROM]->
    (l:Language {name:'Python'})
    RETURN m,l;"""
resultSet = session.run(queryRelationship)

for result in resultSet:
      print("%s from %s" % (result["m"]["text"], result["l"]["name"]))

session.close()
