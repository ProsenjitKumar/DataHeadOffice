from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy, inspect

app = Flask(__name__)
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# #                                                       user     password  127.0.0.1 database
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://prosenjit:prosenjit@localhost/datahead'
# db = SQLAlchemy(app)
#
#
# class Employee(db.Model):
#     __tablename__ = 'employee'
#     id = db.Column('id', db.Integer, primary_key=True)
#     name = db.Column('name', db.Unicode)
#
#     def __init__(self, name):
#         self.name = name
#
#     def __str__(self):
#         return 'name: %s' % self.name
#
#
# class User(db.Model):
#     id = db.Column('id', db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True)
#     email = db.Column(db.String(120), unique=True)
#
#     def __init__(self, username, email):
#         self.username = username
#         self.email = email
#
#     def __str__(self):
#         return '<User %s>' % self.email
#
#
# emp_obj = Employee.query.filter_by(id=3).first()
# emp_obj1 = User.query.filter_by(id=3).first()
# print(emp_obj)
# print(emp_obj1)


# Data inserted
# obj_user = User("Samoli", "kumarisamolirani@gmail.com")
# db.session.add(obj_user)
# db.session.commit()
# print("inserted Data")

# deleted
# delete_data = User.query.filter_by(id=1).first()
# db.session.delete(delete_data)
# db.session.commit()

# Update Datra
# update_data = User.query.filter_by(id=3).first()
# update_data.username = "Samoli Rani"
# db.session.commit()


from attendance.employee_db import history, out, out_count,date_now, time_now1

@app.route('/')
def index():
    return render_template('attendance.html', history=history, out=out, out_count=out_count, date_now=date_now, time_now1=time_now1)


if __name__ == '__main__':
    app.run()

    # from app import app
    # from app.models import Race, db
    # from app.utils import *
    #
    #
    # def historical_records():
    #     df_races, df_circuits, constructors, df_drivers, df_results = extract_to_df_race('results', seasons,
    #                                                                                      races_round)
    #     # Check if row exists in table
    #     exists = db.session.query(db.exists().scalar())
    #     if exists is None:
    #         df_races, df_circuits, constructors, df_drivers, df_results = extract_to_df_race('results', seasons,
    #                                                                                          races_round)
    #         save_races_to_db(df_races, db)
    #     else:
    #         print("The database already contains data of 2016 to current race")
    #
    #
    # def save_races_to_db(df_races, db):
    #     for idx, row in df_races.iterrows():
    #         r = Race()
    #         r.url = df_races.loc[idx, "url"]
    #         r.season = df_races.loc[idx, "season"]
    #         r.raceName = df_races.loc[idx, "raceName"]
    #         db.session.add(r)
    #         try:
    #             db.session.commit()
    #         except Exception as e:
    #             db.session.rollback()
    #             print(str(e))
    #
    #
    # historical_records()