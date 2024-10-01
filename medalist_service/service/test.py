import redis
import json

redis_client = redis.Redis(host='localhost', port=6379, db=0)

# Example message
message = {
    'file_path': 'C:/Users/rosem/Downloads/medal.csv'  # Updated path
}

# Push the message onto the Redis list
redis_client.lpush('medalist_queue', json.dumps(message))
