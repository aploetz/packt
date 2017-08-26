package neo4jHelloWorld;

import org.neo4j.driver.v1.Session;
import org.neo4j.driver.v1.StatementResult;
import org.neo4j.driver.v1.Record;

import static org.neo4j.driver.v1.Values.parameters;

public class Neo4jHelloWorld {

	public static void main(String[] args) {
		//connect to local Neo4j
		Neo4jConnection conn = new Neo4jConnection("192.168.0.100","neodba","flynnLives");
		Session session = conn.getSession();
		
		//create Java language entity
		session.run( "CREATE (:Language {name:{name},version:{ver}})",
		        parameters("name", "Java", "ver", "1.8.0_74"));

		//create relationship from Java language to welcome message
		String createRelationship = "MATCH (m:Message),(l:Language) "
		    + "WHERE m.title = {title} AND l.name={language} "
		    + "CREATE (m)-[:ACCESSED_FROM]->(l);";
		session.run(createRelationship,
				parameters("title", "Welcome", "language", "Java"));

		//query the message and the relationship to Java
		String queryRelationship = "MATCH (m:Message)-[:ACCESSED_FROM]->"
			+ "(l:Language {name:{language}}) "
		   + "RETURN m.title,l.name;";
		StatementResult resultSet = session.run(queryRelationship, parameters("language", "Java"));

		//process result set
		while (resultSet.hasNext())
		{
		    Record result = resultSet.next();
		    System.out.println( result.get("m.title") + " from " + result.get("l.name"));
		}

		session.close();
	}
}
