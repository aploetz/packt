package redisQueryUser;

import java.util.List;
import java.text.SimpleDateFormat;
import java.util.Date;

public class RedisQueryUser {

	public static void main(String[] args) {
		RedisConnection conn = new RedisConnection("127.0.0.1","currentHorseBatteryStaple");
	    System.out.println("Connected to Redis");

	    String key = "packt:logins";
	    String userid = System.getProperty("user.name");
	    //get ip address as the lone command line argument
	    String ip = args[0];
	    String strTime = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss.SSS").format(new Date());
	    String value = userid + " " + ip + " " + strTime;
	    
	    //log user
	    conn.pushToList(key, value);
	    
	    //keep list to a max of 3
	    conn.capList(key, 3);
	    
	    //read login list
	    List<String> logins = conn.getList(key);
	    
	    //output login list
	    for (String user : logins) {
	    	System.out.println(user);
	    }
	    
	    conn.close();
	}
}
