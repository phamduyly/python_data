import psycopg2

conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS users")
cur.execute("CREATE TABLE users(id INTEGER PRIMARY KEY, email TEXT, name TEXT, address TEXT)")import psycopg2
conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS users")
cur.execute("CREATE TABLE users(id INTEGER PRIMARY KEY, email TEXT, name TEXT, address TEXT)")