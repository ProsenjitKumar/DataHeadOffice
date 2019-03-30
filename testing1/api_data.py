import json, urllib.request
from socket import error as SocketError
import errno


# Retirve Json Data from Within API
def api_data():
    url = "https://datahead.herokuapp.com/api/employeers/"
    # url = "http://empisapi.accline.com/api/attendance/getattendancesbydate?date=2019-3-14&deptId=0&desigId=0"
    try:
        response = urllib.request.urlopen(url)
        json_data = json.loads(response.read())
        # result = json_data.get("Result")
    except SocketError as e:
        if e.errno != errno.ECONNRESET:
            raise  # Not error we are looking for
        print("Internet Not Connected")  ## Handle error here.

    fields = [
        #'PID',
        'pid',
        'pname',
        'desig',
        'dept',
        'lts_i',
        'lts_O',
        'p_status'
        #'P_Status'
    ]

    my_data = [list(item[field] for field in fields) for item in json_data]
    # my_data = [list(item[field] for field in fields) for item in result]
    return my_data

# print(api_data())
#
# for i in api_data():
#     print(i[0],i[1],i[2],i[3],)










