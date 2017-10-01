package CassHelloWorld;

import com.datastax.driver.core.BoundStatement;
import com.datastax.driver.core.PreparedStatement;
import com.datastax.driver.core.ResultSet;
import com.datastax.driver.core.Row;
import com.datastax.driver.core.Session;

public class QueryUser {

	public static void main(String[] args) {
		CassandraConnection conn = new CassandraConnection();
		conn.connect("192.168.0.100", "cassdba", "flynnLives");
		Session session = conn.getSession();

		String userID = System.getProperty("user.name");
		String strINSERT = "INSERT INTO packt.logins_by_user "
		    + "(user_id,login_datetime,origin_ip) "
		    + "VALUES (?,dateof(now()),?)";		

		PreparedStatement pIStatement = session.prepare(strINSERT);
		BoundStatement bIStatement = new BoundStatement(pIStatement);
		bIStatement.bind(userID, "192.168.0.119");
				
		String strSELECT = "SELECT * "
				+ "FROM packt.logins_by_user WHERE user_id=? "
				+ "LIMIT 3";
		PreparedStatement pSStatement = session.prepare(strSELECT);
		BoundStatement bSStatement = new BoundStatement(pSStatement);
		bSStatement.bind(userID);
		
		ResultSet rows = conn.query(bSStatement);
		for (Row row : rows) {
			System.out.println(row.getString("user_id") + " " +
					row.getTimestamp("login_datetime") + " " +
					row.getString("origin_ip"));
		}
		conn.close();
	}
}
