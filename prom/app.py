from flask import Flask, jsonify
from prometheus_client import Counter, generate_latest
from flask import Response

app = Flask(__name__)


REQUEST_COUNT = Counter('hello_world_requests', 'Number of requests to Hello World endpoint')

@app.route("/")
def hello():
    REQUEST_COUNT.inc()  
    return "Hello World"

@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {"Content-Type": "text/plain"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)