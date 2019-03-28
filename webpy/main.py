import json, urllib.request
import psycopg2
from psycopg2.extras import execute_values
from time import gmtime, strftime
from datetime import datetime
from socket import error as SocketError
import errno
import web


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

# Retirve Json Data from Within API
url = "https://datahead.herokuapp.com/api/employeers/"
try:
    response = urllib.request.urlopen(url)
    json_data = json.loads(response.read())
except SocketError as e:
    if e.errno != errno.ECONNRESET:
        raise # Not error we are looking for
    print("Internet Not Connected") ## Handle error here.


# connect to the db
try:
    conn = psycopg2.connect("dbname='datahead' user='postgres' host='localhost' password='datahead'")
except:
    print("I am unable to connect to the database")

# cursor
cur = conn.cursor()


fields = [
    'id',
    'name',
    'log_date',
    'log_time',
    'login',
    'logout'
]

# get data from API
my_data = [list(item[field] for field in fields) for item in json_data]


# data insert into database
insert_query = "INSERT INTO employee (id, name, log_date, log_time, login, logout) VALUES %s \
               ON CONFLICT (id) DO UPDATE \
               SET name = excluded.name, log_date = excluded.log_date, log_time = excluded.log_time,\
               login = excluded.login, logout = excluded.logout"

execute_values(cur, insert_query, my_data)
conn.commit()

# execute query
cur.execute("Select id, name, log_date, log_time, login, logout, current_out_time, total_out_time_day, "
            "total_out_time_month, count_total_out_number, absent_name from employee")
db_data = cur.fetchall()


# update data insert
for id, name, log_date, log_time, login, logout, current_out_time, total_out_time_day,\
        total_out_time_month, count_total_out_number, absent_name  in db_data:
    if id and log_date and log_time:
        log_time = str(log_time)
        employee_enter_time = datetime.strptime(log_time, FMT) - datetime.strptime(office_start, FMT)
        if logout:
            if login:
                current_out_time = datetime.strptime(str(login), FMT) - datetime.strptime(str(logout), FMT)
                count = 0
                count = count + 1
                cur.execute("UPDATE employee SET (current_out_time, count_total_out_number) = ('{}', {}) where id={}".format(current_out_time, count, id))
                conn.commit()
                print(id, current_out_time)

    elif id:
        print("Absent Today",id, name)
        cur.execute("UPDATE employee SET absent_name = '{}' where id={}".format(name, id))
        conn.commit()

#
# # last data
# last_data = my_data[-1:]
# last_log_date = last_data[0][2]

# employes all data
history = []
for i in db_data:
    history.append(list(i))

# # employes Today data
# latest_history = []
#
# for h in history:
#     history_last_date = h[2]
#     if str(history_last_date) == str(date_now):
#         latest_history.append(h)
#         print(history_last_date,"==",date_now)
# print(latest_history,'\n')

# Employee percentage Today
cur.execute("SELECT COUNT(absent_name) FROM employee;")
absent_name_count = cur.fetchall()
cur.execute("SELECT COUNT(logout) FROM employee;")
logout_count = cur.fetchall()
cur.execute("SELECT COUNT(login) FROM employee;")
login_count_data = cur.fetchall()
cur.execute("SELECT COUNT(name) FROM employee;")
all_employee = cur.fetchall()
# login count data
for i in login_count_data:
    print("Login Count:",i[0])
    login_count = i[0]
# total employee
for i in all_employee:
    print("All Employee Count:",i[0])
    total_employee = i[0]
print(absent_name_count)
# absent and out count
for i in absent_name_count:
    print("Absent name Count:",i[0])
    absent_count = i[0]
    absent = (absent_count / 100) * total_employee
    active_count = total_employee - i[0]
    active = (active_count / 100) * total_employee

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

# Server running
urls = ('/index.html', 'index')
render = web.template.render('templates/')


class index:
    def GET(self):
        # if last_log_date == date_now:
        #     return render.index(history, latest_history, absent, active, out, absent_count, active_count, out_count,
        #                         date_now, time_now1)
        # return render.test()
        return render.index(history, absent, active, out, absent_count, active_count, out_count,
                                 date_now, time_now1)


if __name__ == "__main__":
    app = web.application(urls, globals())
    print("\n\nrunning")
    app.run()





