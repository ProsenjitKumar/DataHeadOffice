from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
#                                                       user     password  127.0.0.1 database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://prosenjit:prosenjit@localhost/postgres'
db = SQLAlchemy(app)



# class Employee(db.Model):
#     __tablename__ = 'employee'
#     id = db.Column('id', db.Integer, primary_key=True)
#     data = db.Column('name', db.Unicode)


class User(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __str__(self):
        return '<User %s>' % self.username


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

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()