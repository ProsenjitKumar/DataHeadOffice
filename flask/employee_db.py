import psycopg2
from psycopg2.extras import execute_values
import api_data

# connect to the db
try:
    conn = psycopg2.connect("dbname='datahead' user='postgres' host='localhost' password='datahead'")
except:
    print("I am unable to connect to the database")

# cursor
cur = conn.cursor()

# data insert into database
insert_query = "INSERT INTO employee (id, name, log_date, log_time, login, logout) VALUES %s \
               ON CONFLICT (id) DO UPDATE \
               SET name = excluded.name, log_date = excluded.log_date, log_time = excluded.log_time,\
               login = excluded.login, logout = excluded.logout"

execute_values(cur, insert_query, api_data.api_data())
conn.commit()

# execute query
cur.execute("Select id, name, log_date, log_time, login, logout, current_out_time, total_out_time_day, "
            "total_out_time_month, count_total_out_number, absent_name from employee")
db_data = cur.fetchall()