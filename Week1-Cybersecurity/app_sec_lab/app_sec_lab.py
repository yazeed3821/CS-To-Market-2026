import sqlite3
from flask import Flask, request, render_template_string

app = Flask(__name__)

# Initialize an in-memory SQLite database and create a users table with a sample user
def init_db():
    conn = sqlite3.connect(':memory:', check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, password TEXT);")
    cursor.execute("INSERT INTO users (username, password) VALUES ('admin', 'SuperSecretAdminPassword123!');")
    conn.commit()
    return conn

db_conn = init_db()

# HTML template for the login page
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head><title>AppSec Lab</title></head>
<body style="font-family: Arial; margin: 40px;">
    <h2>Login Portal (Training Environment)</h2>
    <form method="POST" action="/login">
        <label>Username:</label><br>
        <input type="text" name="username" style="width: 300px;"><br><br>
        <label>Password:</label><br>
        <input type="password" name="password" style="width: 300px;"><br><br>
        <input type="submit" value="Login">
    </form>
    {% if message %}
        <h3 style="color: {{ color }};">{{ message }}</h3>
    {% endif %}
</body>
</html>
'''

@app.route('/', methods=['GET'])
def index():
    return render_template_string(HTML_TEMPLATE)

# Secured login route using parameterized queries
@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    cursor = db_conn.cursor()

    # SECURE: Using parameterized queries (Prepared Statements)
    # The database engine treats user input strictly as data, never as executable SQL commands.
    query = "SELECT * FROM users WHERE username = ? AND password = ?"
    print(f"\n[DEBUG] Executing parameterized query with values: ({username}, {password})\n")

    cursor.execute(query, (username, password))
    user = cursor.fetchone()

    if user:
        return render_template_string(HTML_TEMPLATE, message=f"Login successful! Welcome: {user[1]}", color="green")
    else:
        return render_template_string(HTML_TEMPLATE, message="Login failed: Invalid credentials", color="red")
if __name__ == '__main__':
    app.run(port=5000, debug=True)