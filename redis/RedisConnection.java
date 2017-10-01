package redisQueryUser;

import java.util.List;
import redis.clients.jedis.Jedis;

public class RedisConnection {
	private Jedis redisConn;

    public RedisConnection() {	
    }
	
    public RedisConnection(String node, String pwd) {
      connect(node,pwd);
    }
    
    public void connect(String node, String pwd) {
    	redisConn = new Jedis(node);
    	redisConn.auth(pwd);
    }

    public String get(String strKey) {
    	return redisConn.get(strKey);
    }

    public void set(String strKey, String strValue) {
    	redisConn.set(strKey, strValue);
    }
    
    public String getSet(String strKey, String strValue) {
    	return redisConn.getSet(strKey, strValue);
    }
    
    public List<String> getList(String strKey) {
    	return redisConn.lrange(strKey, 0, -1);
    }
    
    public void pushToList(String strKey, String strValue) {
    	redisConn.lpush(strKey, strValue);
    }
    
    public void capList(String strKey, int intLen) {
    	redisConn.ltrim(strKey, 0, intLen - 1);
    }

    public void close() {
    	redisConn.close();
    }

}
