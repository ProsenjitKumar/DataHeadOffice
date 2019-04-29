from flask import Flask, render_template, request, flash, redirect, url_for
from requests import Session

from listData.country import countries
from listData.format import image_format, video_format, cus_types, yes_no, color
from faceview.storage.pgsql_system import add_customer
from faceview.storage.insert_db import app_service
from faceview.app_service.app_key import new_app_key


app = Flask(__name__)
sess = Session()



# ---------------- System Admin Page ------------------------------
@app.route('/')
@app.route('/sys-admin')
def sys_admin():
    return render_template('index.html')

# ------------------------- Customer Management: Customer Admin ---------------------
# Registration
@app.route('/customer-registration', methods=['GET', 'POST'])
def cus_registration():
    if request.method == 'POST':
        add_customer(cusID=1, name=request.form['name'], email=request.form['email'], company=request.form['company'],
                     phone=request.form['phone'], address1=request.form['addr_1'], address2=request.form['addr_2'],
                     country=request.form['country'], createdAt='2019-04-12 00:00:00')
        #flash('You were successfully logged in')
        #return redirect(url_for('/'))
        return render_template('cus_management/success.html')
    return render_template('cus_management/cus_registration.html', countries=countries, cus_types=cus_types)


# ------------------------ Update System Setting -----------------
# General setting
@app.route('/general-settings')
def general_settings():
    return render_template('settings/general-settings.html')


# Image setting
@app.route('/image-settings')
def image_setting():
    return render_template('settings/image-setting.html', image_format=image_format, yes_no=yes_no,\
                           color=color)


# video setting
@app.route('/video-settings')
def video_setting():
    return render_template('settings/video-setting.html', video_format=video_format, yes_no=yes_no,
                           color=color)


@app.route('/path-settings')
def path_settings():
    return render_template('settings/path-settings.html')

# -------------------------- Testing -------------------------
# @app.route('/test')
# def test():
#     return render_template('test.html')


# -------------------------- Service Management: App Admin -------------------------
@app.route('/app-id-create', methods=['GET', 'POST'])
def app_id_create():
    if request.method == 'POST':
        app_id = new_app_key()
        app_service(cusId='a', appId='b', appExpire=request.form['date_time'], appKey=app_id,\
                    createdAt='2019-03-11 10:45:12', lastAccess='2019-03-11 10:45:12', notes='New app id created')
        return render_template('service_management/success.html', appId=app_id)
    return render_template('service_management/app_id_create.html', cus_types=cus_types)


if __name__ == '__main__':
    # app.secret_key = os.urandom(24)
    app.config['SESSION_TYPE'] = 'memcached'
    app.config['SECRET_KEY'] = b'_5#y2L"F4Q8z\n\xec]/'
    sess = Session()
    app.run(debug=True, host='localhost')

