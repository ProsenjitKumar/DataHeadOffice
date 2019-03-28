# from flask_pro.api_data import api_data
# # from flask_pro.employee_db import history, absent, active, out, absent_count, active_count, out_count,\
# #                                  date_now, time_now1
#
# print('pagla not ca;lling')
#
# lol = api_data()
#
#
# def pagla():
#     t = 9876
#     return t
import requests

payload = {'name': 'Prosenjit Das'}
r = requests.get('http://empisapi.accline.com/api/attendance/getattendancesbydate?date=2019-3-14&deptId=0&desigId=0')
print(r.text)


