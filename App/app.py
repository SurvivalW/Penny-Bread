
import mysql.connector

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/')
def hello_world():
    return 'Hello World'


def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        port=3307,
        user="root",
        password="your password",
        database="groceryApp"
    )


@app.route("/api/search")
def search_product():
    query = request.args.get("q", "")

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    sql = """
        SELECT 
            p.product_name,
            s.store_name,
            i.price,
            i.stock,
            i.in_stock
        FROM inventory i
        JOIN products p ON i.product_id = p.product_id
        JOIN stores s ON i.store_id = s.store_id
        WHERE p.product_name LIKE %s
        ORDER BY i.price ASC
    """

    cursor.execute(sql, (f"%{query}%",))
    results = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(results)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
    