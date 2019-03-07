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

# time format ****************
FMT = '%H:%M:%S'

# ************ API data retrieve ************
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

# ************** API Json data Insert into database *****************
fields = [
    'id', #integer
    'name', #varchar
    'log_date', #date
    'log_time', #time
    'login', #time
    'logout' #time
]

my_data = [list(item[field] for field in fields) for item in json_data]
insert_query = "INSERT INTO employee (id, name, log_date, log_time, login, logout) VALUES %s \
               ON CONFLICT (id) DO UPDATE \
               SET name = excluded.name, log_date = excluded.log_date, log_time = excluded.log_time,\
               login = excluded.login, logout = excluded.logout"
execute_values(cur, insert_query, my_data)
conn.commit()

# ************* execute query *************
cur.execute("Select id, name, log_date, log_time, login, logout, current_out_time, total_out_time_day, "
            "total_out_time_month, count_total_out_number, absent_name from employee")
db_data = cur.fetchall()


# ************* Update data into Database *************
for id, name, log_date, log_time, login, logout, current_out_time, total_out_time_day,\
        total_out_time_month, count_total_out_number, absent_name  in db_data:
    if id and log_date and log_time:
        log_time = str(log_time)
        employee_enter_time = datetime.strptime(log_time, FMT) - datetime.strptime(office_start, FMT)
        if logout:
            if login:
                current_out_time = datetime.strptime(str(login), FMT) - datetime.strptime(str(logout), FMT)
                cur.execute("UPDATE employee SET current_out_time = '{}' where id={}".format(current_out_time, id))
                conn.commit()
                print(id, current_out_time)

    elif id:
        print("Absent Today", id, name)
        cur.execute("UPDATE employee SET absent_name = '{}' where id={}".format(name, id))
        conn.commit()

# close the cursor
cur.close()

# close the connection
conn.close()

# **************** retrieve every dict item from Database ********************
history = []
for i in db_data:
    history.append(list(i))

# **************** retrieve every dict item from API ********************
for i in json_data:
    print('\n')
    for key, value in i.items():
        print(key,':', value)

# *********** Server running ****************
urls = ('/', 'index')
render = web.template.render('templates/')

# employes data


class index:
    def GET(self):
        return render.index(history)




if __name__ == "__main__":
    app = web.application(urls, globals())
    print("\n\nrunning")
    app.run()

