import redis

r = redis.Redis(
    host='www.plutoese.com',
    port=6379, 
    password='')

print(r.get("celery"))