st =  "abcdefghij"
st = st[:-1]
print(st)

lol = [[1, 'Antu Rani Sarkar', 'Engineer', 'D1', '08:45:54', '05:55:07', 'P_Status']]
la = len(lol)
print(la)


# my data
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

# find total line number and last number of test.txt
num_lines = sum(1 for line in open('test.txt'))
import linecache
a = num_lines - 1
before_the_end_line = linecache.getline('test.txt', a)

# string to array extract last number data
import ast
old_data = ast.literal_eval(before_the_end_line)

old_login = []
for data in old_data:
    old_login.append(data[4])
print("Old:",old_login)
print("new:",lts_i)


# interval calculation

not_logout = []
interval_time = []
interval_time1 = []
everybody = []

all_data = interval_time + interval_time1 + not_logout

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


# test.txt file remove when time = 23:59:59
import time, os
current_time = time.localtime()
now = time.strftime('%H:%M:%S', current_time)
if now == '23:59:59':
    os.remove('test.txt')
else:
    print("now: ", now)
