import psycopg2
import time
import datetime
from http.server import HTTPServer, BaseHTTPRequestHandler


# ***** connect to the db *******
try:
    conn = psycopg2.connect("dbname='datahead' user='postgres' host='localhost' password='datahead'")
except:
    print("I am unable to connect to the database")

# cursor
cur = conn.cursor()

# execute query
cur.execute("Select id, name, log_date, log_time from employeer")
rows = cur.fetchall()

# close the cursor
cur.close()

# close the connection
conn.close()

# Employe List
emploey_dict = {r[0]:r[1] for r in rows}
emploee_all_name = [r[1] for r in rows]
print(emploee_all_name)
print(emploey_dict)

print(rows)
history = []
for i in rows:
    print(list(i))
    history.append(list(i))



# # employe in and out
# in_active_employee_serial = int()
# in_active_employee_name = ''
#
# # First in time employee
# currentDT = datetime.datetime.now()
# in_employe = int(input("Which employee want to enter: "))
# in_time_employee = currentDT.strftime("%a, %b %d, %Y") + ' ' + currentDT.strftime("%I:%M:%S %p")
# for key in emploey_dict.keys():
#     if in_employe == key:
#         print("Active:", emploey_dict[key], in_time_employee)
#         in_active_employee_name = emploey_dict[key]
#         in_active_employee_serial = key
#         with open('output.txt', mode='a+') as file_write_read:
#             file_write_read.write("{} Active {} \n".format(in_active_employee_name, in_time_employee))
#
# # Out time Employee
# out_time_employee = currentDT.strftime("%I:%M:%S %p")
# out_employe = int(input("Which employee want to go out: "))
# if in_active_employee_serial == out_employe:
#     print(in_active_employee_name, 'Out of office Now.', out_time_employee)
#     with open('output.txt', mode='a+') as file_write_read:
#         file_write_read.write("{} Out {} \n".format(in_active_employee_name, out_time_employee))
#
# #print(emploee_all_name)
#
# today_all_history = open('output.txt').read()
#print(today_all_history)


# # Localhost run
# class DataHeadServer(BaseHTTPRequestHandler):
#
#     def do_GET(self):
#         #if self.path == '/':
#         if self.path == '/index.html':
#             self.path = '/index.html'
#         try:
#             file_to_open = open(self.path[1:]).read()
#             file_to_open = file_to_open.format(in_active_employee_name=emploee_all_name)
#                                                # emploee_all_name=emploee_all_name,
#                                                # today_all_history=today_all_history)
#             self.send_response(200)
#         except:
#             file_to_open = "File Not Found"
#             self.send_response(404)
#         self.end_headers()
#         self.wfile.write(bytes(file_to_open, 'utf-8'))
#
#
# httpd = HTTPServer(('localhost', 8080), DataHeadServer)
# httpd.serve_forever()
