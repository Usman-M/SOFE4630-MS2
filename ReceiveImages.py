import redis        # pip install redis
import io;
import base64

ip="34.118.133.98"
r = redis.Redis(host=ip, port=6379, db=0,password='sofe4630u')

keys = r.keys("*")

for key in keys:
    value = r.get(key)
    decoded_value=base64.b64decode(value)

    with open(key, "wb") as f:
        f.write(decoded_value)
    
    print(f'Image received, check {key}')
