import web
import json, urllib.request
import datetime
from time import gmtime, strftime
import psycopg2
from psycopg2.extras import execute_values


# todays date and time
date_now = datetime.date.today()
time_now = strftime("%H:%M:%S", gmtime())
print("Today's Date: ", date_now)
print("Current Time: ", time_now)

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
historical_data = cur.fetchall()


# ************* Historical data Retrieve *************
for id, name, log_date, log_time, login, logout, current_out_time, total_out_time_day,\
        total_out_time_month, count_total_out_number, absent_name  in historical_data:
    print(id)
    print(name)
    print('\n')
    break

# close the cursor
cur.close()

# close the connection
conn.close()

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
        return render.index(json_data)


if __name__ == "__main__":
    app = web.application(urls, globals())
    print("\n\nrunning")
    app.run()

