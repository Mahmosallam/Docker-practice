from flask import Flask, jsonify
import requests
import psycopg2

app = Flask(__name__)

# Connect to DB
def get_db_connection():
    conn = psycopg2.connect(
        host="db-service",
        database="appdb",
        user="appuser",
        password="apppass"
    )
    return conn

@app.route("/orders")
def get_orders():
    # Call Product Service
    products = requests.get("http://product-service:5000/products").json()

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, product_id, quantity FROM orders;")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    orders = []
    for r in rows:
        product = next((p for p in products if p["id"] == r[1]), None)
        orders.append({
            "order_id": r[0],
            "product": product["name"] if product else "Unknown",
            "quantity": r[2]
        })

    return jsonify(orders)

@app.route("/")
def home():
    return "Order Service Connected to Product + DB"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
