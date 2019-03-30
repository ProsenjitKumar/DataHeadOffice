from flask import Flask, render_template, request, redirect, url_for
from employee_db import insert_data_into_db, current_data, conn, cur

app = Flask(__name__)
insert_data_into_db()


@app.route('/employee.html')
def index():
    return render_template('attendance.html', current_data=current_data)


@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == "POST":
        cur.execute("select * from history where log_date = '{}'".format(request.form['search']))
        db_history_data = cur.fetchall()
        history = []
        for r in db_history_data:
            history.append(list(r))
        render_value = render_template('search.html', history=history)
    return render_value


if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True, port=8080, host='localhost')

