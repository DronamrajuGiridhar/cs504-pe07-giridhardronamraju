import mysql.connector

username = input("Enter your username: ")
password = input("Enter your password: ")

db = mysql.connector.connect(
    host="127.0.0.1",
    port=6603,
    user="root",
    password="root",
    database="dbe"
)

cursor = db.cursor()

query = """
SELECT * FROM users
WHERE username = %s
AND password = %s
"""

cursor.execute(query, (username, password))

result = cursor.fetchone()

if result:
    print("Login successful!")
else:
    print("Invalid username or password.")

db.close()