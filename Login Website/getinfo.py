#python -m pip install flask
from flask import Flask, render_template, request
import sqlite3
import hashlib


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello', methods=['POST'])
def hello():
    username = request.form['username']
    password = request.form['password'] 
    # Process the form data here
    print(f"Username: {username}, Password: {password}")
    conn = sqlite3.connect("undb.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            passwordhash TEXT NOT NULL
        )
    """)
    passwordhash = hashlib.sha256(password.encode()).hexdigest()
    cursor.execute("INSERT INTO users (username, passwordhash) VALUES (?, ?)", (username, passwordhash))
    conn.commit()
    conn.close()
    return render_template('index.html')

@app.route('/goodbye', methods=['POST'])
def goodbye():
    username = request.form['username']
    password = request.form['password'] 
    # Process the form data here
    print(f"Username: {username}, Password: {password}")
    conn = sqlite3.connect("undb.db")
    cursor = conn.cursor()
    passwordhash = hashlib.sha256(password.encode()).hexdigest()
    cursor.execute("SELECT * FROM users WHERE username = ? AND passwordhash = ?", (username, passwordhash))
    result = cursor.fetchall()
    if len(result) > 0:
        print("Login successful")
        return render_template('success.html')
    else:    
        print("Login failed")
        return render_template('index.html', error="Invalid username or password")




if __name__ == '__main__':
    app.run()    