import mysql.connector

conn = mysql.connector.connect(
    host="your-rds-endpoint",
    user="admin",
    password="Kvmk26112003",
    database="demo"
)

cursor = conn.cursor()
cursor.execute("SELECT * FROM students")

for row in cursor.fetchall():
    print(row)

conn.close()
