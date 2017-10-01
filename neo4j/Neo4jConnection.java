package neo4jHelloWorld;

import org.neo4j.driver.v1.AuthTokens;
import org.neo4j.driver.v1.Driver;
import org.neo4j.driver.v1.GraphDatabase;
import org.neo4j.driver.v1.Session;

public class Neo4jConnection {
	private Driver driver;
	private Session session;
	
	public Neo4jConnection() {	
	}
	
	public Neo4jConnection(String node, String user, String pwd) {
		connect(node,user,pwd);
	}
	
	public void connect(String node, String user, String pwd) {
		driver = GraphDatabase.driver( "bolt://" + node + ":7687", AuthTokens.basic( user, pwd ) );
		session = driver.session();
	}
	
    public Session getSession() {
    	return session;
    }

	public void close() {
		session.close();
		driver.close();
	}
}
