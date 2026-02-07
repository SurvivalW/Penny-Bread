from flask import Flask, jsonify, request
from flask_cors import CORS

import mysql.connector

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
CORS(app)

@app.route("/") 
def index(): 
    return render_template("index.html")


def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        port=3307,
        user="root",
        password="password",
        database="groceryApp"
    )


@app.route("/api/search", methods=["GET"])
def search_product():
    query = request.args.get("q", "")
    
    if not query:
        return jsonify([])

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
        WHERE p.product_name LIKE %s AND i.stock > 0
        ORDER BY i.price ASC
        LIMIT 20
    """

    cursor.execute(sql, (f"%{query}%",))
    results = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(results)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
    


# CORS(app)

# MOCK_PRODUCTS = [
#     {
#         "id": 1,
#         "item": "Milk",
#         "store": "Kroger",
#         "price": 3.49,
#         "stock": 12
#     },
#     {
#         "id": 2,
#         "item": "Milk",
#         "store": "Walmart",
#         "price": 3.19,
#         "stock": 20
#     },
#     {
#         "id": 3,
#         "item": "Bread",
#         "store": "Target",
#         "price": 2.29,
#         "stock": 8
#     }
# ]

# api/search mentioned twice so need to combine it
# @app.route("/api/search")
# def search():
#     query = request.args.get("q", "").lower()

#     results = [
#         p for p in MOCK_PRODUCTS
#         if query in p["item"].lower()
#     ]

#     return jsonify(results)

# if __name__ == "__main__":
#     app.run(debug=True)