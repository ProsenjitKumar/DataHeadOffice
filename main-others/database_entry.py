import psycopg2
import time
import datetime
from http.server import HTTPServer, BaseHTTPRequestHandler
from jinja2 import Template

# ***** connect to the db *******
try:
    conn = psycopg2.connect("dbname='datahead' user='postgres' host='localhost' password='datahead'")
except:
    print("I am unable to connect to the database")

# cursor
cur = conn.cursor()

# execute query
cur.execute("Select id, name from employers")
rows = cur.fetchall()

# close the cursor
cur.close()

# close the connection
conn.close()

# Employe List
emploey_dict = {r[0]:r[1] for r in rows}
employee_name = {r[1] for r in rows}
print(employee_name)

#template = Template(employee_name)
# Localhost run
class DataHeadServer(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/':
            self.path = '/index1.html'
        try:
            file_to_open = open(self.path[1:]).read()

            file_to_open = file_to_open.format(employee_name=employee_name)

            self.send_response(200)

        except:
            file_to_open = "File Not Found"
            self.send_response(404)
        self.end_headers()
        self.wfile.write(bytes(file_to_open, 'utf-8'))
        #return template.render(employee_name)

httpd = HTTPServer(('localhost', 8080), DataHeadServer)
httpd.serve_forever()
