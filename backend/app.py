from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

def get_products():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name, price FROM products")
    products = [{'name': row[0], 'price': row[1]} for row in cursor.fetchall()]
    conn.close()
    return products

@app.route('/products')
def products():
    return jsonify(get_products())

if __name__ == '__main__':
    app.run(host='0.0.0.0')

