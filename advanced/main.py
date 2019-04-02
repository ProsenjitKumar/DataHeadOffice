# from flask_pro.employee_db import history, absent, active, out, absent_count, active_count, out_count,\
#                                  date_now, time_now1
#
# from flask import Flask, render_template
#
# app = Flask(__name__)
#
#
# @app.route("/")
# @app.route("/employee")
# def home():
#     return render_template("employee.html",
#                            history=history,
#                            absent=absent, active=active, out=out,
#                            absent_count=absent_count, active_count=active_count,
#                            out_count=out_count, date_now=date_now, time_now1=time_now1
#                            )
#
#
# if __name__ == '__main__':
#     app.run(debug=True)

# import datetime
# mylist = []
# today = datetime.date.today()
# mylist.append(today)
# print(mylist[0]) # print the date object, not the container ;-)

my_data = [[100, 'Prosenjit Das', 'researcher', 'D1', '10:11:12', '01:10:48', 'P_Status'],
           [20, 'Arif Khan', 'Managing Director', 'D1', '09:14:41', '11:03:06', 'P_Status'],
           [13, 'Mr. hasib', 'Managing Director', 'D1', '00:14:49', '00:00:00', 'P_Status'],
           [1, 'Antu Sarkar', 'Engineer', 'D1', '00:11:54', '00:55:07', 'P_Status'],
           [25, 'Avijit', 'Managing Director', 'D1', '00:08:10', '00:00:00', 'P_Status']]


lts_i = []
lts_O = []
pid = []
for data in my_data:
    lts_i.append(data[4])
    lts_O.append(data[5])
    pid.append(data[0])


not_logout = []
interval_time = []
interval_time1 = []

from datetime import datetime, timedelta
FMT = '%H:%M:%S'
for login, logout, did, ar_data in zip(lts_i, lts_O, pid, my_data):
    if login:
      # old_login = login
        if pid and logout > '00:00:00' and login < logout:
            if login != login:
              # if login: or not equal login. old_login < login:
                durations = datetime.strptime(str(logout), FMT) - datetime.strptime(str(login), FMT)
                print(logout,'-',login,'---',durations)
                ar_data = ar_data + [durations]
                interval_time.append(ar_data)
        elif pid and logout > '00:00:00' and login > logout:
            add_time = timedelta(hours=12) + datetime.strptime(str(logout), FMT)
            logout = '{:%H:%M:%S}'.format(add_time)
            # print('logut',logout)
            # print('login',login)
            print('nlogout',logout)

            durations = datetime.strptime(str(logout), FMT) - datetime.strptime(str(login), FMT)
            # durations1 = datetime.strptime(str(logout), FMT) - datetime.strptime(str(login), FMT)
            ar_data = ar_data + [durations]
            interval_time1.append(ar_data)
            print(durations)
            # print(durations1)
            # print(login)
        elif pid and logout == '00:00:00':
            not_logout.append(ar_data)


# def convert24(str1):
#     # Checking if last two elements of time
#     # is AM and first two elements are 12
#     if str1[-2:] == "AM" and str1[:2] == "12":
#         return "00" + str1[2:-2]
#
#         # remove the AM
#     elif str1[-2:] == "AM":
#         return str1[:-2]
#
#         # Checking if last two elements of time
#     # is PM and first two elements are 12
#     elif str1[-2:] == "PM" and str1[:2] == "12":
#         return str1[:-2]
#
#     else:
#
#         # add 12 to hours and remove PM
#         return str(int(str1[:2]) + 12) + str1[2:8]
#
#     # Driver Code
#
#
# print(convert24("12:00:00 AM"))

# import time
# timestamp = time.strftime('%H:%M:%S') - '12:00:00'
# print(timestamp)

all_data = interval_time + not_logout + interval_time1
print(all_data)
print(interval_time1)
# print(interval_time)
# print("\n")
# print(not_logout)
print('\n')

# import time
# start_time = time.time()
# print(start_time)
# # your script
# elapsed_time = time.time() - start_time
# print(time.strftime("%H:%M:%S", time.gmtime(elapsed_time)))
#
# import datetime
# start = datetime.datetime.now()
# # some code
# end = datetime.datetime.now()
# print(end)
# elapsed = end - start
# print(elapsed)
#
#
# import time
# start_time = time.time()
# e = int(time.time() - start_time)
# print('{:02d}:{:02d}:{:02d}'.format(e // 3600, (e % 3600 // 60), e % 60))

# import datetime
# def calc_timing(original_function):
#     def new_function(*args,**kwargs):
#         start = datetime.datetime.now()
#         x = original_function(*args,**kwargs)
#         elapsed = datetime.datetime.now()
#         print("Elapsed Time = {0}".format(elapsed-start))
#         return x
#     return new_function()
#
# @calc_timing
# def a_func(*variables):
#     print("do something big!")



#
# import time
#
# def stopwatch(seconds):
#     start = time.time()
#     time.clock()
#     elapsed = 0
#     while elapsed < seconds:
#         elapsed = time.time() - start
#         print("loop cycle time: %f, seconds count: %02d" % (time.clock() , elapsed) )
#         time.sleep(1)
#
# stopwatch(20)

# datetime.strptime(str(logout), FMT)
# from dateutil.relativedelta import relativedelta
# import datetime
# today = datetime.date.today()
# rd = relativedelta(today, datetime.strptime(str(logout), FMT))
# print("comment created %(years)d years, %(months)d months, %(days)d days ago" % rd.__dict__)
#
#
# import datetime
#
# today   = datetime.date.today()
# futdate = datetime.date(2016, 8, 10)
#
# now     = datetime.datetime.now()
# mnight  = now.replace(hour=0, minute=0, second=0, microsecond=0)
# seconds = (mnight - now).seconds
# days    = (futdate - today).days
# hms     = str(datetime.timedelta(seconds=seconds))
#
# print ("%d days %s" % (days, hms))










