from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

# Connect to Database
def get_db_connection():
    conn = psycopg2.connect(
        host="db-service",
        database="appdb",
        user="appuser",
        password="apppass"
    )
    return conn

@app.route("/products")
def get_products():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, name, price FROM products;")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify([{"id": r[0], "name": r[1], "price": r[2]} for r in rows])

@app.route("/")
def home():
    return "Product Service Connected to DB"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
