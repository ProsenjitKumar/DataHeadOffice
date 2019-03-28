import psycopg2
from psycopg2.extras import execute_values
from datetime import datetime
from .api_data import api_data


# todays date and time
now = datetime.now()
date_now = now.strftime("%Y-%m-%d")
time_now = now.strftime("%H:%M:%S")
time_now1 = now.strftime("%H:%M:%S %p")
print("Today's Date: ", date_now)
print("Current Time: ", time_now)
print('\n')

# ofiice time
office_start = '10:00:00'
office_end = '06:00:00'

# time format
FMT = '%H:%M:%S'

# connect to the db
try:
    conn = psycopg2.connect("dbname='datahead' user='postgres' host='localhost' password='datahead'")
except:
    print("I am unable to connect to the database")

# cursor
cur = conn.cursor()


# data insert into database
def insert_data_into_db():
    insert_query = "INSERT INTO attendance (pid, pname, desig, dept, lts_i, lts_O, p_status) VALUES %s \
                   ON CONFLICT (pid) DO UPDATE \
                   SET pname = excluded.pname, desig = excluded.desig, dept = excluded.dept,\
                   lts_i = excluded.lts_i, lts_O = excluded.lts_O, p_status = excluded.p_status"

    execute_values(cur, insert_query, api_data())
    conn.commit()

    # execute query
    cur.execute("Select pid, pname, desig, dept, lts_i, lts_O, p_status from attendance")
    db_data = cur.fetchall()
    return db_data


# update data insert
for pid, pname, desig, dept, lts_i, lts_O, p_status  in insert_data_into_db():
    if pid and lts_i:
        employee_enter_time = datetime.strptime(str(lts_i), FMT) - datetime.strptime(office_start, FMT)
        if lts_O is None:
            if lts_i:
                interval_time = datetime.strptime(str(lts_i), FMT) - datetime.strptime(str(lts_O), FMT)
                cur.execute("UPDATE attendance SET interval = '{}' where pid={}".format(interval_time, pid))
                conn.commit()
                print(pid, interval_time)

    # elif pid:
    #     print("Absent Today",pid, pname)
    #     cur.execute("UPDATE employee SET absent_name = '{}' where id={}".format(pname, pid))
    #     conn.commit()


# employes all data
history = []
for i in insert_data_into_db():
    history.append(list(i))


# cur.execute("SELECT COUNT(absent_name) FROM employee;")
# absent_name_count = cur.fetchall()
cur.execute("SELECT COUNT(lts_O) FROM attendance;")
logout_count = cur.fetchall()
cur.execute("SELECT COUNT(lts_i) FROM attendance;")
login_count_data = cur.fetchall()
cur.execute("SELECT COUNT(pname) FROM attendance;")
all_employee = cur.fetchall()

# login count data
for i in login_count_data:
    print("Login Count:",i[0])
    login_count = i[0]

# total employee
for i in all_employee:
    print("All Employee Count:",i[0])
    total_employee = i[0]
# print(absent_name_count)

# absent and out count
# for i in absent_name_count:
#     print("Absent name Count:",i[0])
#     absent_count = i[0]
#     absent = (absent_count / 100) * total_employee
#     active_count = total_employee - i[0]
#     active = (active_count / 100) * total_employee

# logout count
for i in logout_count:
    print("Total Logout Count:",i[0])
    total_out_count = i[0]
    out_count = total_out_count - login_count
    out = (out_count / 100) * total_employee
    # still out employee
    print("Still Out",out_count)


# close the cursor
cur.close()

# close the connection
conn.close()