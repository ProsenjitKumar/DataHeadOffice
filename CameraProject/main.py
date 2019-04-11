from flask import Flask, render_template, request, flash, redirect, url_for
from requests import Session

from country.retrieve import countries
from faceview.storage.pgsql_system import add_customer

app = Flask(__name__)
sess = Session()



# ---------------- System Admin Page ------------------------------
@app.route('/')
@app.route('/sys-admin')
def sys_admin():
    return render_template('index.html')

# ------------------------- Customer Management ---------------------
# Registration
@app.route('/customer-registration', methods=['GET', 'POST'])
def cus_registration():
    cus_types = ['Trial', 'Regular', 'Priority']
    if request.method == 'POST':
        add_customer(cusID=1, name=request.form['name'], email=request.form['email'], company=request.form['company'],
                     phone=request.form['phone'], address1=request.form['addr_1'], address2=request.form['addr_2'],
                     country=request.form['country'], createdAt='2019-04-12 00:00:00')
        return render_template('cus_management/success.html')
    return render_template('cus_management/cus_registration.html', countries=countries, cus_types=cus_types)


# ------------------------ setting -----------------
# Image setting
@app.route('/image-settings')
def image_setting():
    return render_template('settings/image-setting.html')


# video setting
@app.route('/video-settings')
def video_setting():
    return render_template('settings/video-setting.html')


@app.route('/test')
def test():
    return render_template('test.html')


if __name__ == '__main__':
    app.run(debug=True, host='localhost')

