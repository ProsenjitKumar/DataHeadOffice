import requests
from flask import Flask, render_template, request
from attendance.api_data import my_data
import json, urllib.request
from socket import error as SocketError
import errno

app = Flask(__name__)


@app.route('/employee.html')
def index():
    return render_template('attendance.html', current_data=my_data)


@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == "POST":
        searchData = ("{}".format(request.form['search']))
        url = "http://empisapi.accline.com/api/attendance/getattendancesbydate?date={}&deptId=0&desigId=0".format(
            searchData)
        try:
            response = urllib.request.urlopen(url)
            json_data = json.loads(response.read())
            result = json_data.get("Result")
        except SocketError as e:
            if e.errno != errno.ECONNRESET:
                raise  # Not error we are looking for
            print("Internet Not Connected")  ## Handle error here.

        fields = [
            # 'PID',
            'PID',
            'pname',
            'desig',
            'dept',
            'lts_i',
            'lts_O',
            'P_Status'
            # 'P_Status'
        ]

        history_my_data = [list(item[field] for field in fields) for item in result]
        render_value = render_template('search.html', history=history_my_data, searchData=searchData)

    return render_value


if __name__ == '__main__':
    # app.jinja_env.auto_reload = True
    # app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True, port=8080, host='localhost')

