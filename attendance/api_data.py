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
    # 'PID',
    'pid',
    'pname',
    'desig',
    'dept',
    'lts_i',
    'lts_O',
    # 'P_Status'
    'p_status'
]

my_data = [list(item[field] for field in fields) for item in result]




