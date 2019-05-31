//Import with psycopg2 
//Create connection
//Create cur. 
// Define variable 
//pRINT 
import psycopg2
conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()
cur.execute('SELECT * FROM notes')
one = cur.fetchone()
notes = cur.fetchall()
all = cur.fetchall()
print(notes)
cur.close()
