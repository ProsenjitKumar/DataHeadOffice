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

# all_data = interval_time + not_logout + interval_time1
# print(all_data)
# print(interval_time1)
# # print(interval_time)
# # print("\n")
# # print(not_logout)
# print('\n')

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

# import os
# with open('test.txt', 'rb') as f:
#     f.seek(-2, os.SEEK_END)
#     while f.read(1) != b'\n':
#         f.seek(-2, os.SEEK_CUR)
#     last_line = f.readline().decode()
# f.close()
# print(last_line)
# print(my_data)

# Write CSV file
# kwargs = {'newline': ''}
# mode = 'w'
# if sys.version_info < (3, 0):
#     kwargs.pop('newline', None)
#
# mode = 'wb'
# with open('test.csv', mode, **kwargs) as fp:
#     writer = csv.writer(fp)
#     # writer.writerow(["your", "header", "foo"])  # write header
#     writer.writerows(lts_i)
#
# # Read CSV file
# kwargs = {'newline': ''}
# mode = 'r'
# if sys.version_info < (3, 0):
#     kwargs.pop('newline', None)
#     mode = 'rb'
# with open('test.csv', mode, **kwargs) as fp:
#     reader = csv.reader(fp)
#     # next(reader, None)  # skip the headers
#     data_read = [row for row in reader]
#
# print(data_read)

# import unicodecsv as csv
# # Write CSV file
# with open('test.csv', 'w', newline='') as fp:
#     writer = csv.writer(fp, encoding='utf-8')
#     # writer.writerow(["your", "header", "foo"])  # write header
#     writer.writerows(my_data)

# print(before_the_end_line)
# write read csv file
# with open('test.csv', 'a', newline='') as myfile:
#     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
#     wr.writerow(before_the_end_line)


# import pandas
# df = pandas.read_csv('test.csv', sep=',',header=None)

#print(df)
# print('\n')

#print(df)
# for i, line in enumerate(df):
#     print(i, line)
#
#print(before_the_end_line)
# with open('test.txt') as fp:
#     pagla = fp.readline()
# print(pagla)
# old_lts_i = []
# #
# for data in df:
#     print(data)
#     old_lts_i.append(data[4])
# content = [x.strip() for x in before_the_end_line]
# print(before_the_end_line)




my_data = [[100, 'Prosenjit Das', 'researcher', 'D1', '05:22:12', '01:10:48', 'P_Status'],
           [20, 'Arif Khan', 'Managing Director', 'D1', '12:25:11', '11:03:06', 'P_Status'],
           [13, 'Mr. hasib', 'Managing Director', 'D1', '05:25:19', '02:00:00', 'P_Status'],
           [1, 'Antu Sarkar', 'Engineer', 'D1', '08:15:54', '05:55:07', 'P_Status'],
           [50, 'Samoli Das', 'Engineer', 'D1', '05:16:54', '00:00:00', 'P_Status'],
           [10, 'Antu Sarkar', 'Engineer', 'D1', '04:12:54', '03:55:07', 'P_Status']
           ]
# my current data
lts_i = []
lts_O = []
pid = []
for data in my_data:
    lts_i.append(data[4])
    lts_O.append(data[5])
    pid.append(data[0])

# old Data *****************************************************************
# write read text file
with open('test.txt', 'a') as fp:
    fp.write(str(my_data))
    fp.write('\n')

# test.txt file remove when time = 23:59:59
import time, os
current_time = time.localtime()
now = time.strftime('%H:%M:%S', current_time)
if now == '23:59:59':
    os.remove('test.txt')
else:
    print("now: ", now)

# fine total line number and last number of test.txt
num_lines = sum(1 for line in open('test.txt'))
# print(num_lines)
import linecache
a = num_lines - 1
before_the_end_line = linecache.getline('test.txt', a)



import ast
old_data = ast.literal_eval(before_the_end_line)

old_login = []
for data in old_data:
    old_login.append(data[4])
print("Old:",old_login)
print("new:",lts_i)


# interval or duration calculation

not_logout = []
interval_time = []
interval_time1 = []
everybody = []

# all data
with open('all_data.txt', mode='w') as pagla:
    for data in my_data:
        pagla.write(str(data))
        pagla.write('\n')
pagla.close()

from datetime import datetime, timedelta
FMT = '%H:%M:%S'
for login, logout, did, ar_data, old_l in zip(lts_i, lts_O, pid, my_data, old_login):
    if login:
        everybody.append(ar_data)
        if did and logout > '00:00:00' and login < logout:
            if login != old_l:
                add_time = timedelta(hours=12) + datetime.strptime(str(login), FMT)
                add_login = '{:%H:%M:%S}'.format(add_time)
                durations = datetime.strptime(str(add_login), FMT) - datetime.strptime(str(logout), FMT)
                print(did, add_login,'-',logout,'---',durations)
                nar_data = ar_data + [durations]
                print(durations)
                with open('all_data.txt', mode='r') as pagla_value:
                    for line in pagla_value:
                        pagla.write(line.replace(str(nar_data), str(ar_data)))
                        pagla.close()
        elif did and logout > '00:00:00' and login > logout:
            if login != old_l:
                durations = datetime.strptime(str(login), FMT) - datetime.strptime(str(logout), FMT)
                nar_data = ar_data + [durations]
                interval_time1.append(nar_data)
                print(did, durations)
                print(nar_data)
                print(ar_data)
                with open('duration.txt', mode='w') as pagla_value:
                    pagla_value.write(str(interval_time1))
                    pagla_value.close()

        elif pid and logout == '00:00:00':
            not_logout.append(ar_data)



all_data = interval_time + interval_time1 + not_logout + everybody
print(all_data)



