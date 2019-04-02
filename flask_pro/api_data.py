import json, urllib.request
from socket import error as SocketError
import errno


# Retirve Json Data from Within API
def api_data():
    url = "https://datahead.herokuapp.com/api/employeers/"
    try:
        response = urllib.request.urlopen(url)
        json_data = json.loads(response.read())
    except SocketError as e:
        if e.errno != errno.ECONNRESET:
            raise  # Not error we are looking for
        print("Internet Not Connected")  ## Handle error here.

    fields = [
        'pid',
        'pname',
        'desig',
        'dept',
        'lts_i',
        'lts_O',
        'p_status'
    ]

    my_data = [list(item[field] for field in fields) for item in json_data]
    return my_data

print(api_data())

