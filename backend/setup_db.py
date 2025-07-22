import sqlite3

conn = sqlite3.connect('products.db')
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS products (name TEXT, price REAL)')
cursor.execute('INSERT INTO products (name, price) VALUES (?, ?)', ('Laptop', 999.99))
cursor.execute('INSERT INTO products (name, price) VALUES (?, ?)', ('Smartphone', 499.99))
cursor.execute('INSERT INTO products (name, price) VALUES (?, ?)', ('Headphones', 199.99))
conn.commit()
conn.close()

