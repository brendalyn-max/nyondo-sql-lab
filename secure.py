import sqlite3
conn = sqlite3.connect('nyondo_stock.db')

# Secure search function
def search_product_safe(name):
    query = "SELECT * FROM products WHERE name LIKE ?"
    rows = conn.execute(query, (f"%{name}%",)).fetchall()
    print("Query:", query, "with param:", name)
    print("Result:", rows, "\n")
    return rows

# Secure login function
def login_safe(username, password):
    query = "SELECT * FROM users WHERE username=? AND password=?"
    row = conn.execute(query, (username, password)).fetchone()
    print("Query:", query, "with params:", username, password)
    print("Result:", row, "\n")
    return row

# --- Tests: all must return [] or None ---
print('Test 1:', search_product_safe("' OR 1=1--"))
print('Test 2:', search_product_safe("' UNION SELECT id,username,password,role FROM users--"))
print('Test 3:', login_safe("admin'--", 'anything'))
print('Test 4:', login_safe("' OR '1'='1", "' OR '1'='1"))
