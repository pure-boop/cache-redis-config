import os
import redis
from dotenv import load_dotenv

load_dotenv()

class RedisConfig:
    def __init__(self):
        self.host = os.getenv('REDIS_HOST', 'localhost')
        self.port = int(os.getenv('REDIS_PORT', 6379))
        self.db = int(os.getenv('REDIS_DB', 0))
        self.password = os.getenv('REDIS_PASSWORD', None)
        self.redis_client = self._create_redis_client()

    def _create_redis_client(self):
        return redis.Redis(
            host=self.host,
            port=self.port,
            db=self.db,
            password=self.password,
            decode_responses=True
        )

    def get_client(self):
        return self.redis_client

if __name__ == "__main__":
    redis_config = RedisConfig()
    client = redis_config.get_client()
    client.set('test_key', 'test_value')
    print(client.get('test_key'))