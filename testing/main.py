from flask import Flask, render_template
from testing.employee_db import insert_data_into_db, current_data

app = Flask(__name__)
insert_data_into_db()


@app.route('/')
def index():
    return render_template('attendance.html', current_data=current_data)


if __name__ == '__main__':
    app.run()

