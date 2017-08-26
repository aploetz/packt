package neo4jHelloWorld;

import org.neo4j.driver.v1.Session;
import org.neo4j.driver.v1.StatementResult;
import org.neo4j.driver.v1.Record;

import static org.neo4j.driver.v1.Values.parameters;

public class Neo4jISS53 {

	public static void main(String[] args) {
		//connect to local Neo4j
		Neo4jConnection conn = new Neo4jConnection("192.168.0.100","neodba","flynnLives");
		Session session = conn.getSession();
		
		//CREATE mission Expedition 52
		String createMission = "CREATE (:Mission {name:{name}})";
		session.run(createMission,parameters("name","ISS-52/53 (Soyuz)"));

		//CREATE FLOWN_ON edges for astronauts (below) to Expedition 52
		String createRelationship = "MATCH (m:Mission),(a:Astronaut) "
			+ "WHERE m.name={mname} AND a.name={aname} "
		    + "CREATE (a)-[:FLEW_ON]->(m)";
		session.run(createRelationship, parameters("mname","ISS-52/53 (Soyuz)","aname","Joseph M. Acaba"));
		session.run(createRelationship, parameters("mname","ISS-52/53 (Soyuz)","aname","Mark T. Vande Hei"));
		session.run(createRelationship, parameters("mname","ISS-52/53 (Soyuz)","aname","Randolph J. Bresnik"));

		//query the mission and the edges to the Astronauts
		String queryRelationship = "MATCH (m:Mission {name:{name}})<-[:FLEW_ON]-"
		    + "(a:Astronaut) RETURN m.name,a.name;";
		StatementResult resultSet = session.run(queryRelationship, parameters("name", "ISS-52/53 (Soyuz)"));

		//process result set
		while (resultSet.hasNext())
		{
		    Record result = resultSet.next();
		    System.out.println( result.get("a.name") + " flew on " + result.get("m.name"));
		}

		session.close();
	}
}
