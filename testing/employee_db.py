import psycopg2
from psycopg2.extras import execute_values
from .api_data import api_data


# connect to the db
try:
    conn = psycopg2.connect("dbname='datahead' user='postgres' host='localhost' password='datahead'")
except:
    print("I am unable to connect to the database")

# cursor
cur = conn.cursor()


# data insert into database
def insert_data_into_db():

    insert_query = "INSERT INTO employee (pid, pname, desig, dept, lts_i, lts_O, p_status) VALUES %s \
                    ON CONFLICT (pid) DO UPDATE SET \
                    (pname, desig, dept, lts_i, lts_O, p_status) = \
                    (EXCLUDED.pname, EXCLUDED.desig, EXCLUDED.dept, EXCLUDED.lts_i, EXCLUDED.lts_O, EXCLUDED.p_status) \
                    RETURNING *"

    #for i in api_data():
        #print(i[0], i[1], i[2], i[3], )
        #insert_query = "SELECT merge_db({}, '{}', '{}', '{}')".format(i[0], i[1], i[2], i[3], i[4], i[5], i[6])
    # execute_values(cur, insert_query, api_data())
    execute_values(cur, insert_query, api_data())
        #cur.execute(insert_query)
    conn.commit()

    # execute query
    cur.execute("Select pid, pname, desig, dept, lts_i, lts_O, p_status, interval_time, total_interval_time, out_count\
     from employee where today = current_date")
    db_data = cur.fetchall()

    return db_data


current_data = []
for i in insert_data_into_db():
    current_data.append(list(i))










