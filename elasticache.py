# Import the Redis package
import redis

redisEndpoint = 'YOUR_REDIS_ENDPOINT'
# Get the port and host from the endpoint string
PORT = redisEndpoint[-4:];
HOST = redisEndpoint[:-5];

# Configure Redis connection
def config_redis_connection():
    r = redis.Redis(
        host=HOST,
        port=PORT)
    print('Configured Redis node connection: ')
    print(r)
    return r

# Main program
def main():
    redis_connection = config_redis_connection()
if __name__ == '__main__':
    main()
