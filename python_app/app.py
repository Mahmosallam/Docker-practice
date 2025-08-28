import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    app_name = os.getenv('APP_NAME', 'unknown app')
    app_env = os.getenv('APP_ENV', 'development')
    return f"Hello from {app_name}! Environment: {app_env}"

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port)