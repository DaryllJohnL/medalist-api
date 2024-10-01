import redis

# Connect to Redis
redis_client = redis.Redis(host='localhost', port=6379, db=0)

# Retrieve all messages from the queue
messages = redis_client.lrange('medalist_queue', 0, -1)

# Print messages
for message in messages:
    print(message.decode('utf-8'))  # Decode bytes to string
