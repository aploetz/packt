package redisQueryUser;

public class RedisHelloWorld {

	public static void main(String[] args) {
		RedisConnection conn = new RedisConnection("127.0.0.1","currentHorseBatteryStaple");
	    System.out.println("Connected to Redis");

	    String key = "packt:welcome";
	    String newMessage = "Hello world from Java!";
	    
	    //GET value stored in packt:welcome
	    System.out.println("Displaying current welcome message...");
//	    String message = conn.get("packt:welcome");
	    
	    //SET new value packt:welcome
	    String message = conn.getSet(key,newMessage);
	    System.out.println(message);
	    System.out.println("Writing \"" + newMessage + "\" to Redis...");
	    
	    //GET value stored in packt:welcome
	    System.out.println("Displaying the new welcome message...");
	    message = conn.get("packt:welcome");
	    System.out.println(message);
	    
	    conn.close();
	}

}
