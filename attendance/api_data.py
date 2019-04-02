import json, urllib.request
from socket import error as SocketError
import errno
import datetime


# Retirve Json Data from Within API

mylist = []
today = datetime.date.today()
mylist.append(today)
currentDate = mylist[0]
url = "http://empisapi.accline.com/api/attendance/getattendancesbydate?date={}&deptId=0&desigId=0".format(currentDate)
try:
    response = urllib.request.urlopen(url)
    json_data = json.loads(response.read())
    result = json_data.get("Result")
except SocketError as e:
    if e.errno != errno.ECONNRESET:
        raise  # Not error we are looking for
    print("Internet Not Connected")  ## Handle error here.

fields = [
    'PID',
    'pname',
    'desig',
    'dept',
    'lts_i',
    'lts_O',
    'P_Status'
]

my_data = [list(item[field] for field in fields) for item in result]


lts_i = []
lts_O = []
pid = []
for data in my_data:
    lts_i.append(data[4])
    lts_O.append(data[5])
    pid.append(data[0])


not_logout = []
interval_time = []

from datetime import datetime
FMT = '%H:%M:%S'
for login, logout, did, ar_data in zip(lts_i, lts_O, pid, my_data):
    if login:
        if pid and logout > '00:00:00':
            durations = datetime.strptime(str(login), FMT) - datetime.strptime(str(logout), FMT)
            ar_data = ar_data + [durations]
            interval_time.append(ar_data)
        elif pid and logout == '00:00:00':
            not_logout.append(ar_data)


all_data = interval_time + not_logout






