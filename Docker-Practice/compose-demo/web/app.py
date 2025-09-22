from flask import Flask
import redis, os

app = Flask(__name__)

r = redis.Redis(host=os.getenv("REDIS_HOST", "redis"), port=6379, decode_responses=True)

@app.route("/")
def index():
    count = r.incr("hits")
    return f"Hello! This page has been visited {count} times.\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)