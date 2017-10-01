package CassHelloWorld;

import com.datastax.driver.core.Cluster;
import com.datastax.driver.core.Session;
import com.datastax.driver.core.ResultSet;
import com.datastax.driver.core.BoundStatement;
	
public class CassandraConnection {
	private Cluster cluster;
	private Session session;

    public CassandraConnection() {	
    }
	
    public CassandraConnection(String node, String user, String pwd) {
      connect(node,user,pwd);
    }
    
    public void connect(String node, String user, String pwd) {
      cluster = Cluster.builder()
        .addContactPoint(node)
        .withCredentials(user,pwd)
        .build();
      session = cluster.connect();
    }

    public ResultSet query(String strQuery) {
      return session.execute(strQuery);
    }
    	
    public void close() {
      cluster.close();
    }
    
    public ResultSet query(BoundStatement bStatement) {
	  return session.execute(bStatement);
	}
		
	public void insert(BoundStatement bStatement) {
	  session.execute(bStatement);
	}
		
	public Session getSession() {
	  return session;
	}
}
