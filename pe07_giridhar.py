import mysql.connector

username = input("Enter your username: ")
password = input("Enter your password: ")

query = (
    "SELECT * FROM users WHERE username = '"
    + username
    + "' AND password = '"
    + password
    + "';"
)

db = mysql.connector.connect(
    host="127.0.0.1",
    port=6603,
    user="root",
    password="root",
    database="dbe"
)

cursor = db.cursor()

print("\nGenerated Query:")
print(query)

cursor.execute(query)

result = cursor.fetchone()

if result is not None:
    print("Login successful!")
else:
    print("Invalid username or password.")

db.close()