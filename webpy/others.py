import web
import json, urllib.request
import psycopg2
from psycopg2.extras import execute_values
from time import gmtime, strftime
from datetime import datetime
from socket import error as SocketError
import errno


# todays date and time
now = datetime.now()
date_now = now.strftime("%Y-%m-%d")
time_now = now.strftime("%H:%M:%S")
time_now1 = now.strftime("%H:%M:%S %p")
print("Today's Date: ", date_now)
print("Current Time: ", time_now)
print('\n')

# ofiice time **************
office_start = '10:00:00'
office_end = '06:00:00'

# # total employee ****************
# total_employee = 135

# time format ****************
FMT = '%H:%M:%S'

# Retirve Json Data from Withing API
url = "https://datahead.herokuapp.com/api/employeers/"
try:
    response = urllib.request.urlopen(url)
    json_data = json.loads(response.read())
except SocketError as e:
    if e.errno != errno.ECONNRESET:
        raise # Not error we are looking for
    print("Internet Not Connected") ## Handle error here.



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
my_data = [list(item[field] for field in fields) for item in json_data]

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


# def employee_percentage(absent_count, active_count, out_count):
#     absent = (absent_count / 100) * total_employee
#     active = total_employee - active_count / 100
#     out = total_employee - out_count / 100
#     return absent, active, out

# def absent_percentage(absent_count):
#     absent = (absent_count / 100) * total_employee
#     return absent

# def employee_percentage(absent_count, active_count, out_count):
#     absent = (absent_count / 100) * total_employee
#     active = total_employee - active_count / 100
#     out = total_employee - out_count / 100
#     return absent, active, out



#print(db_data[19])
#print(historical_data)

# print(history)
# print(history[1][3])
# for i in history:
#     for j in i:
#         print(j)


# absent today
# absent = 45.36
# active = 70.68
# out = 12.39

# emp_position = {'absent': 45.26, 'active': 65.12, 'out': 12.65}
# print(emp_position[0])
# # for key, value in emp_position.items():
# #     print(value)



# last data ***********************************
last_data = my_data[-1:]
# print(last_data[0][2])
last_log_date = last_data[0][2]

# employes data *******************************
history = []
for i in db_data:
    #print(list(i))
    history.append(list(i))
#print(history)

# employes Today data *******************************
latest_history = []

for h in history:
    # print("id",h[0])
    # if h[0] == 18:
    #     print("date:", h[2])
    #     print("last Dat:", last_log_date)
    #     print("last Dat:", date_now)
    history_last_date = h[2]
    #
    if str(history_last_date) == str(date_now):
        latest_history.append(h)
        print(history_last_date,"==",date_now)
    #latest_history.append(h[2])
print(latest_history,'\n')

# ******************************* Employee percentage Today ************************************************************
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
    #absent_percentage(i[0])
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

# history_last_date = []
# for i in latest_history:
#     # print(i)
#     if i == date_now:
#         history_last_date.append(i)
# print(history_last_date)


# cur.execute("select log_date from employee")
# logdate = cur.fetchall()
# for i in logdate:
#     #print(i[0])
#     current_log_date = i[0]
# today_couurent_employee_data


# for i in json_data:
#     print('\n')
#     for key, value in i.items():
#         print(key,':', value)

# if current_log_date == date_now:
#     #print(current_log_date)
#     #print(date_now)
#     print("soman soman")


# close the cursor
cur.close()

# close the connection
conn.close()

# Server running
urls = ('/index.html', 'index')
render = web.template.render('templates/')


class index:
    def GET(self):
        if last_log_date == date_now:
            return render.index(history, latest_history, absent, active, out, absent_count, active_count, out_count,
                                date_now, time_now1)
        return render.test()


if __name__ == "__main__":
    app = web.application(urls, globals())
    print("\n\nrunning")
    app.run()





