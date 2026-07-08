import psycopg2

conn = psycopg2.connect(
    dbname="companydb",
    user="admin",
    password="admin123",
    host="127.0.0.1",
    port=5432
)

print("Connection successful!")
conn.close()