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


import sqlite3
conn = sqlite3.connect('nyondo_stock.db')

# --- Validation helpers ---
def valid_name(name):
    if not isinstance(name, str): return False
    if len(name) < 2: return False
    if any(c in name for c in "<>;"): return False
    return True

def valid_price(price):
    try:
        return float(price) > 0
    except:
        return False

def valid_username(username):
    if not isinstance(username, str): return False
    if " " in username: return False
    if len(username) == 0: return False
    return True

def valid_password(password):
    if not isinstance(password, str): return False
    if len(password) < 6: return False
    return True

# --- Secure functions with validation ---
def search_product_safe(name):
    if not valid_name(name):
        print("Error: invalid product name")
        return None
    query = "SELECT * FROM products WHERE name LIKE ?"
    rows = conn.execute(query, (f"%{name}%",)).fetchall()
    print("Result:", rows, "\n")
    return rows

def login_safe(username, password):
    if not valid_username(username):
        print("Error: invalid username")
        return None
    if not valid_password(password):
        print("Error: invalid password")
        return None
    query = "SELECT * FROM users WHERE username=? AND password=?"
    row = conn.execute(query, (username, password)).fetchone()
    print("Result:", row, "\n")
    return row

# --- Test cases ---
print("Test 1:", search_product_safe("cement"))        
print("Test 2:", search_product_safe(""))              
print("Test 3:", search_product_safe("<script>"))      
print("Test 4:", login_safe("admin", "admin123"))      
print("Test 5:", login_safe("admin", "ab"))            
print("Test 6:", login_safe("ad min", "pass123"))      
