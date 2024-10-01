import pandas as pd
from pymongo import MongoClient
import redis
import time
import json

class MongoDB:
    def __init__(self, uri, db_name):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        self.collection = self.db['medalists']

    def insert_record(self, record):
        # Check for duplicates
        if not self.collection.find_one({'name': record['name'], 'event': record['event']}):
            self.collection.insert_one(record)

class RedisQueue:
    def __init__(self, host='localhost', port=6379, db=0):
        self.redis = redis.Redis(host=host, port=port, db=db)

    def enqueue(self, message):
        self.redis.lpush('medalist_queue', json.dumps(message))

    def dequeue(self):

        message = self.redis.rpop('medalist_queue')
        return json.loads(message) if message else None

class CSVProcessor:
    def __init__(self, mongodb, redis_queue):
        self.mongodb = mongodb
        self.redis_queue = redis_queue

    def process_csv(self, file_path):
        df = pd.read_csv(file_path)
        for _, row in df.iterrows():
            record = {
                'name': row['name'],
                'event': row['event'],
                'medal': row['medal']
            }
            self.mongodb.insert_record(record)
            self.redis_queue.enqueue(record)

def main():
    mongodb = MongoDB('mongodb://localhost:27017/', 'medal_db')
    redis_queue = RedisQueue()
    processor = CSVProcessor(mongodb, redis_queue)

    while True:
        message = redis_queue.dequeue()
        if message:
            print(f'Processing: {message}')
            # Further processing if needed
        else:
            time.sleep(1)  # Wait before checking the queue again

if __name__ == "__main__":
    main()
