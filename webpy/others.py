import web
import json, urllib.request, requests
import datetime
from time import sleep
import psycopg2
import jsoncomment
from psycopg2.extras import execute_values
import time
from time import gmtime, strftime


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
my_data = [list(item[field] for field in fields) for item in json_data]

cur.execute("select id from employee")
emp_id = cur.fetchall()
main_id = [{i[0]} for i in emp_id]
api_id = []
db_id = []
for i in main_id:
    for key in i:
        db_id.append(key)

my_data = [list(item[field] for field in fields) for item in json_data]
for api in my_data:
    api_id.append(api[0])
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
historical_data = cur.fetchall()


for id, name, log_date, log_time, login, logout, current_out_time, total_out_time_day,\
        total_out_time_month, count_total_out_number, absent_name  in historical_data:
    pass

# close the cursor
cur.close()

# close the connection
conn.close()

# Server running
urls = ('/', 'index')
render = web.template.render('templates/')

# employes data


class index:
    def GET(self):
        return render.index(historical_data)


if __name__ == "__main__":
    app = web.application(urls, globals())
    print("\n\nrunning")
    app.run()





