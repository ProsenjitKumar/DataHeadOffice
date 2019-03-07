import web
import json, urllib.request
import psycopg2
from psycopg2.extras import execute_values
from time import gmtime, strftime
from datetime import datetime, timedelta

# todays date and time
date_now = datetime.today().now()
time_now = strftime("%H:%M:%S", gmtime())
print("Today's Date: ", date_now)
print("Current Time: ", time_now)
print('\n')

# ofiice time **************
office_start = '10:00:00'
office_end = '06:00:00'

# total employee ****************
total_employee = 135

# time format ****************
FMT = '%H:%M:%S'

# Retirve Json Data from Withing API

url = "https://datahead.herokuapp.com/api/employeers/"
response = urllib.request.urlopen(url)
json_data = json.loads(response.read())


# ***** connect to the db *******
try:
    conn = psycopg2.connect("dbname='datahead' user='postgres' host='localhost' password='datahead'")
except:
    print("I am unable to connect to the database")

# cursor
cur = conn.cursor()


fields = [
    'id', #integer
    'name', #varchar
    'log_date', #date
    'log_time', #timestamp
    'login', #timestamp
    'logout' #timestamp
]

# **************** calculation *********************
my_data = [tuple(item[field] for field in fields) for item in json_data]

# cur.execute("select id from employee")
# emp_id = cur.fetchall()
# main_id = [{i[0]} for i in emp_id]
# api_id = []
# db_id = []
# for i in main_id:
#     for key in i:
#         db_id.append(key)
#
# my_data = [list(item[field] for field in fields) for item in json_data]
# for api in my_data:
#     api_id.append(api[0])
# print(api_id)
# print(db_id)
# last_data = []
# for i in my_data:
#     #print(i[0])
#     last_data.append(i[0])
#     #print('\n')
#     # for j in i:
#     #     print()
# print(last_data[-1:])

#last_data = my_data[-1:]
# for i in my_data:
#     #print(i[0])
#     last_data.append(i)
#     #print('\n')
#     # for j in i:
#     #     print()
# print(last_data[-1:])
# most_last_data = last_data[-1:]
# print('\n')
# print(most_last_data)
# #print(my_data)
# new_id = [item for item in api_id if item not in db_id]
# print("new Here:", new_id)


# insert_query = "INSERT INTO employee (id, name, log_date, log_time, login, logout) VALUES %s"
# execute_values(cur, insert_query, my_data)
# conn.commit()

# ************************ for last data ***********************************
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

# cur.execute("insert into employee (id, current_out_time) values (%s, %s)", (606, '06:01:33'))
# conn.commit()

# db_data = [i[0] for i in historical_data]
# print(db_data)

for id, name, log_date, log_time, login, logout, current_out_time, total_out_time_day,\
        total_out_time_month, count_total_out_number, absent_name  in db_data:
    # db_data.append(id)
    # db_data.append(name)
    # db_data.append(log_date)
    # db_data.append(log_time)
    # db_data.append(login)
    # db_data.append(logout)
    # db_data.append(current_out_time)
    # db_data.append(total_out_time_day)
    # db_data.append(total_out_time_month)
    # db_data.append(count_total_out_number)
    # db_data.append(absent_name)
    if id and log_date and log_time:
        log_time = str(log_time)
        employee_enter_time = datetime.strptime(log_time, FMT) - datetime.strptime(office_start, FMT)
        #print("you are late today: ",id,  employee_enter_time)
        if logout:
            #print(id, logout)
            # something do

            if login:
                current_out_time = datetime.strptime(str(login), FMT) - datetime.strptime(str(logout), FMT)
                count = 0
                count = count + 1
                cur.execute("UPDATE employee SET (current_out_time, count_total_out_number) = ('{}', {}) where id={}".format(current_out_time, count, id))
                conn.commit()
                print(id, current_out_time)
                # print(count)
                # if count_total_out_number < count:
                #     count_total_out_number = count_total_out_number
                # cur.execute("UPDATE employee SET count_total_out_number = {} where id = {}".format(count, id))

    elif id:
        print("Absent Today",id, name)
        cur.execute("UPDATE employee SET absent_name = '{}' where id={}".format(name, id))
        conn.commit()

#print(db_data[19])
#print(historical_data)
history = []
for i in db_data:
    #print(list(i))
    history.append(list(i))
# print(history)
# print(history[1][3])
# for i in history:
#     for j in i:
#         print(j)


# absent today
absent = 45.36
active = 70.68
out = 12.39

# emp_position = {'absent': 45.26, 'active': 65.12, 'out': 12.65}
# print(emp_position[0])
# # for key, value in emp_position.items():
# #     print(value)

# close the cursor
cur.close()

# close the connection
conn.close()

# calender *****************************
import calendar
import re

myCal = calendar.HTMLCalendar(calendar.SUNDAY)
myStr = myCal.formatmonth(2009, 7)
#str_r = calendar.TextCalendar(calendar.SUNDAY)
str_r = calendar.HTMLCalendar(calendar.SUNDAY)
c = str_r.formatmonth(2019, 1)

# Server running
urls = ('/', 'index')
render = web.template.render('templates/')

# employes data


class index:
    def GET(self):
        return render.index(history, absent, active, out, c)


if __name__ == "__main__":
    app = web.application(urls, globals())
    print("\n\nrunning")
    app.run()





