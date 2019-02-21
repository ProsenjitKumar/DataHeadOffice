print('datahead')
import psycopg2


# connect to the db
try:
    conn = psycopg2.connect("dbname='datahead' user='postgres' host='localhost' password='datahead'")
    print('database connected')
except:
    print("I am unable to connect to the database")

# cursor
cur = conn.cursor()

# execute query
cur.execute("insert into employers (id, name) values (%s, %s)", (4, "Newton"))

cur.execute("Select id, name from employers")
rows = cur.fetchall()
for r in rows:
    print(f"id {r[0]} name {r[1]}")

# close the cursor
cur.close()

# close the connection
conn.close()

