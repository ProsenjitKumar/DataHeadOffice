# from flask import Flask, request
# from flask_restful import Resource, Api
# from sqlalchemy import create_engine
# from json import dumps
# from flask.ext.jsonpify import jsonify
# import psycopg2
#
# # ***** connect to the db *******
# try:
#     conn = psycopg2.connect("dbname='datahead2' user='postgres' host='localhost' password='datahead'")
# except:
#     print("I am unable to connect to the database")
#
# # cursor
# cur = conn.cursor()
#
# # execute query
# cur.execute("Select id, name, ldt, lts, eio from employeers")
#
#
# app = Flask(__name__)
# api = Api(app)
#
#
# class Employees(Resource):
#     def get(self):
#         # conn = db_connect.connect()  # connect to database
#         # query = conn.execute("select * from employees")  # This line performs query and returns json result
#         return {'employees': [i[0] for i in cur.cursor.fetchall()]}  # Fetches first column that is Employee ID
#
#
# class Tracks(Resource):
#     def get(self):
#         # conn = db_connect.connect()
#         query = cur.execute("Select id, name, ldt, lts, eio from employeers")
#         result = {'data': [dict(zip(tuple(query.keys()), i)) for i in query.cursor]}
#         return jsonify(result)
#
#
# class Employees_Name(Resource):
#     def get(self, employee_id):
#         # conn = db_connect.connect()
#         query = conn.execute("select * from employeers where id =%d " % int(id))
#         result = {'data': [dict(zip(tuple(query.keys()), i)) for i in query.cursor]}
#         return jsonify(result)
#
#
# api.add_resource(Employees, '/employees')  # Route_1
# api.add_resource(Tracks, '/tracks')  # Route_2
# api.add_resource(Employees_Name, '/employees/<employee_id>')  # Route_3
#
# if __name__ == '__main__':
#     app.run(port='5002')


from flask import Flask
app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return "<h1>Hello Home Page!</h1>"


@app.route("/about")
def about():
    return "<h1>About Page!</h1>"


if __name__ == '__main__':
    app.run(debug=True)


