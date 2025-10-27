import psycopg2

try:
    conn = psycopg2.connect(
        host="localhost",
        database="customer_churn",
        user="postgres",
        password="newpassword123", 
        port="5432"
    )
    print("✅ Connection successful!")
    conn.close()
except Exception as e:
    print("❌ Connection failed:", e)
