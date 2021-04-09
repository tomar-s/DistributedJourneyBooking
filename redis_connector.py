import redis
r = redis.Redis(host='localhost', port=6379, db=0)
r.mset({"Croatia": "Zagreb", "Bahamas": "Nassau"})
value = r.get("Bahamas")
print(value)