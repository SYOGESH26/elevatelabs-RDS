import mysql.connector

conn = mysql.connector.connect(
    host="elevate.cli40464cqa5.eu-north-1.rds.amazonaws.com",
    user="admin",
    password="Kvmk26112003",
    database="demo"
)

cursor = conn.cursor()
cursor.execute("SELECT * FROM students")

for row in cursor.fetchall():
    print(row)

conn.close()
