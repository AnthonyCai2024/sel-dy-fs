import redis

r = redis.Redis(host='36.137.225.245', port=6376, db=1, password='mtic0756-dev')


# add set
def add_set(key, value: set):
    r.sadd(key, *value)


def get_set(key):
    return r.smembers(key)


# remove set
def remove_set(key, value):
    r.srem(key, value)
