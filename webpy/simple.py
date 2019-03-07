# import web
#
#
# urls = ("/.*", "hello")
# app = web.application(urls, globals())
#
# class hello:
#     def GET(self):
#         return 'Hello, world!'
#
# if __name__ == "__main__":
#     app.run()

# class Hello(object):
#     def __init__(self, req):
#         self.request = req
#
#     def get(self):
#         return '''<form method="POST">
#                         Your Name: <input type="text" name="name">
#                         <input type="submit">
#                    </form>'''
#
#     def post(self):
#         return 'Hello %s!' % self.request.params['name']
#
#
# hello = rest_controller(Hello)
import psycopg2

import web
import json, urllib.request, requests, io
from datetime import datetime
from time import sleep

from psycopg2.extras import execute_values

now = datetime.now
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
# print(data)
# print(json.dumps(data))
# print(type(data))
# print(data[1])
# print(type(data[0]))
# print("\n\n")
# new_dict = data[0]
# print(new_dict)
# for i in new_dict:
#     print(new_dict[i])

# with open('data.json', 'w') as fp:
#     json.dump(api_data, fp, indent=4, ensure_ascii=False)

# data = []
# with open('data.json') as f:
#     for line in f:
#         data.append(json.loads(line))

fields = [
    'id', #varchar
    'name', #BigInt
    'log_date', #BigInt Nullable
    'log_time', #JSONB
    'login',
    'logout'
]


cur.execute("select id from employee")
emp_id = cur.fetchall()
main_id = [{i[0]} for i in emp_id]
# print(emp_id[0])
# print(main_id)
# print(main_id[0])
api_id = []
db_id = []
for i in main_id:
    for key in i:
        db_id.append(key)
        #print("from Database ",key)

#my_api_data = [list(item[field] for field in fields) for item in json_data]
my_data = [list(item[field] for field in fields) for item in json_data]
for api in my_data:
    api_id.append(api[0])
print(api_id)
print(db_id)

new_id = [item for item in api_id if item not in db_id]


# for id in api_id:
#     if id in db_id:
#         print("have")
#     else:
#         new_id.append(id)


# for a_id in api_id:
#     for d_id in db_id:
#         if a_id == d_id:
#
print(new_id)
# if api_id == db_id:
#     print("same")
# else:
#     print("New come here")
#     #my_data = [list(item[field] for field in fields) for item in json_data]
#     insert_query = "INSERT INTO employee (id, name, log_date, log_time, login, logout) VALUES %s"
#     execute_values(cur, insert_query, my_data)
#     conn.commit()

    # if api[0] == key:
            #     print("Existing ID")
            # else:
            #     print("Something to do")
            #print("From API", api[0])
# for i in my_data:
#     print("From API", i[0])


# for item in data:
#     my_data = [item[field] for field in fields]
#     insert_query = "INSERT INTO employee VALUES (%s, %s, %s, %s, %s, %s)"
#     cursor.execute(insert_query, tuple(my_data))


# with open('data.json') as json_file:  
#     data = json.load(json_file)
#     for p in data['people']:
#         print('Name: ' + p['name'])
#         print('Website: ' + p['website'])
#         print('From: ' + p['from'])
#         print('')

# for i in data:
#     print('\n')
#     for key, value in i.items():
#         print(key,':', value)

# Server running ******************************************************
# urls = ('/', 'index')
# render = web.template.render('templates/')

# employes data


# class index:
#     def GET(self):
#         return render.index(api_data)
#
#
# if __name__ == "__main__":
#     app = web.application(urls, globals())
#     print("\n\nrunning")
#     app.run()


 # *************************************************** datetime checked
# x = datetime.datetime.now()
# y = datetime.datetime.now().time()
# date_now = datetime.date.today()
# #print(time.gmtime())
# current = strftime("%H:%M:%S", gmtime())
# print(current)
# print(y)
# print(x.now())
# print(date_now)
# print(x.today())
# print(x.ctime())



#  *************************************************** Json data Insert
# with open('data.json', 'w') as fp:
#     json.dump(json_data, fp, indent=4, separators=(',', ':'), ensure_ascii=False)
#
# fp.close()
#
#
# data = []
# with open('data.json') as f:
#     for line in f:
#         data.append(json.loads(line))

#list_data = []

# for item in json_data:
#     my_data = [item[field] for field in fields]
#     #print(my_data)
#     list_data.append(my_data)
    # insert_query = "INSERT INTO employee VALUES (%s, %s, %s, %s, %s, %s)"
    # cur.execute(insert_query, my_data)
    # conn.commit()
#print(list_data)
#print('\n')
#print(list_data[1][4])
#for i in list_data:
    #print(i)
    #'\n'
    # print(i[0])
    # print(i[1])
    # print(i[2])
    # print(i[3])
    # print(i[4])
    # print(i[5])
    # cur.execute("insert into employee (id, name, log_date, log_time, login, logout) values (%s, %s, %s, %s, %s, %s)", (i[0], i[1], i[2], i[3], i[4], i[5]))
    # conn.commit()


# for data in json_data:
# 	print('\n')
# 	for key, values in data.items():
# 		pass
# 		#print(values)


#cur.execute("insert into employee (id, name) values (%s, %s)", (7, "Akash"))
# commit the transaction
#conn.commit()


# print(historical_data)
# for data in historical_data:
#     print(data, type(data))
# #
# data = {i[0]:i[1] for i in historical_data}
# print(data)


# if [ "$( psql -tAc "SELECT 1 FROM pg_database WHERE datname='DB_NAME'" )" = '1' ]
# then
#     echo "Database already exists"
# else
#     echo "Database does not exist"
# fi
# for i in my_data:
#     print(i[0])
    # cur.execute("if[select id from employee where id='i[0]']\
    #             then\
    #                 echo 'Id already exists into table'\
    #             else\
    #                 insert_query = "INSERT INTO employee (id, name, log_date, log_time, login, logout) VALUES %s"\
    #             fi")


# something do
# print(login)
# if current_out_time.days < 0:
#     tdiff = timedelta(days=0,
#                       seconds=current_out_time.seconds, microseconds=current_out_time.microseconds)
#     print(id, tdiff)
# cur.execute("insert into employers (id, name) values (%s, %s)", (7, "Akash"))
# cur.execute("INSERT INTO employee (current_out_time) VALUES (%s)", (current_out_time))