# setup.py
import sqlite3

# Connect to database (creates nyondo_stock.db if it doesn’t exist)
conn = sqlite3.connect('nyondo_stock.db')

# Create products table
conn.execute('''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    price REAL NOT NULL
)
''')

# Insert 5 products in one go
conn.executemany(
    'INSERT INTO products (name, description, price) VALUES (?, ?, ?)',
    [
        ('Cement (bag)', 'Portland cement 50kg bag', 35000),
        ('Iron Sheet 3m','Gauge 30 roofing sheet 3m long', 110000),
        ('Paint 5L', 'Exterior wall paint white 5L', 60000),
        ('Nails 1kg', 'Common wire nails 1kg pack', 12000),
        ('Timber 2x4', 'Pine timber plank 2x4 per metre', 25000),
    ]
)

conn.commit()

# Confirm products
rows = conn.execute('SELECT * FROM products').fetchall()
for r in rows:
    print(r)
