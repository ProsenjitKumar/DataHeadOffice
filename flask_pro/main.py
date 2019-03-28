from flask import Flask, render_template
from flask_pro.employee_db import history, absent, active, out,\
    absent_count, active_count, out_count,\
    date_now, time_now1


# server run
app = Flask(__name__)

# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://prosenjit:prosenjit@localhost/datahead'
# db = SQLAlchemy(app)
#
#
# # Database Create
# class MyCompany(db.Model):
#     pid = db.Column('id', db.Integer, primary_key=True)
#     pname = db.Column(db.String(50), index=True)
#     pname = db.Column(db.String(50), index=True)
#     login = db.Column(Time, index=True)
#     logout = db.Column(Time, index=True)
#     interval_time = db.Column(Time, index=True)
#     total_interval_time = db.Column(Time, index=True)
#     interval_time = db.Column(Time, index=True)
#     interval_time = db.Column(Time, index=True)
#
#     def __init__(self, id, name, login, logout):
#         self.id = id
#         self.name = name
#         self.login = login
#         self.logout = logout
#
#     def __str__(self):
#         return '<User %s>' % self.id
#
#
# db.create_all()
# db.session.commit()

# Database Call from employee_db


# data = MyCompany.query.filter_by(id=28).first()
# print(data)


@app.route("/")
@app.route("/employee")
def home():
    return render_template("employee.html", history=history,
                           absent=absent, active=active, out=out,
                           absent_count=absent_count, active_count=active_count,
                           out_count=out_count, date_now=date_now, time_now1=time_now1
                           )


if __name__ == '__main__':
    app.run(debug=True)


