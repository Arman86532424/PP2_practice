import psycopg2

conn = psycopg2.connect(host="localhost", dbname = "postgres", user = "postgres", password = "1234", port = "5555")

cur = conn.cursor()

cur.execute(""" CREATE TABLE IF NOT EXISTS phone_book (
            id INT PRIMARY KEY,
            name VARCHAR(255),
            age INT,
            number VARCHAR(255)
);
""")
conn.commit()

cur.close()
conn.close()