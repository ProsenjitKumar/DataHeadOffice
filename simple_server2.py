# import simpletable
#
# test_data = [str(x) for x in range(20)]
# formatted_data = simpletable.fit_data_to_columns(test_data, 5)
# table = simpletable.SimpleTable(formatted_data)
# html_page = simpletable.HTMLPage(table)
# html_page.save("index1.html")

# list = ['a', 'b', 'c']
# # Insert newlines between every element, with a * prepended
# inserted_list = '\n'.join(['* ' + x for x in list])
#
# template = '''<html>
# <title>Attributes</title>
# %s
# </html>''' %(inserted_list)
# print(template)
#
# a = {}
#
# id_input = int(input("Id Name: "))
# name_input = int(input("Name: "))
#
# a[] = id_input, name_input
# print(a)

# n = int(input())          #n is the number of items you want to enter
# d ={}
# for i in range(n):
#     text = input().split()     #split the input text based on space & store in the list 'text'
#     d[text[0]] = text[1]       #assign the 1st item to key and 2nd item to value of the dictionary
# print(d)


# n=int(input())
# d = dict()
# for i in range(n):
#     data = input().split(' ')
#     d[data[0]] = data[1]
# for keys,values in d.items():
#     print(keys)
#     print(values)

# record = int(input("Enter the student record need to add :"))
# stud_data={}
#
# for i in range(0,record):
#     Name = input("Enter the student name :").split()
#     Age = input("Enter the {} age :".format(Name))
#     Grade = input("Enter the {} grade :".format(Name)).split()
#     Nam_key =  Name[0]
#     Age_value = Age[0]
#     Grade_value = Grade[0]
#     stud_data[Nam_key] = {Age_value,Grade_value}
#
# print(stud_data)


# n = 3
# d = dict(input().split() for _ in range(n))
# print(d)


# d = {}
# count = 0
# car_colours = input("Car: ")
# while car_colours != '':
#     if d.has_key(car_colours):
#         d[car_colours] = d[car_colours] + 1
#     else:
#         d[car_colours] = 1
#     count = count + 1
#     car_colours = input("Car: ")
#
# for k,v in d.iteritems():
#     print('Cars that are ' + k + ": " + str(v))


# from collections import defaultdict
#
# print("Enter car colours and ^C when done...")
# try:
#     car_count = defaultdict(int)
#     while True:
#         car_colour = input("Car colour: ")
#         car_count[car_colour] += 1
# except KeyboardInterrupt:
#     print("Done with input, now the result")
#
# for c in car_count:
#     print("Cars that are %s: %d" % (c, car_count[c]))

# mydict = {'a': 'hello', 'b': 'world'}
# faka = {}
#
# for x in mydict:
#     val = faka[x]
#     print(val)

# print('datahead')
# import psycopg2
#
#
# # connect to the db
# try:
#     conn = psycopg2.connect("dbname='datahead' user='postgres' host='localhost' password='datahead'")
#     print('database connected')
# except:
#     print("I am unable to connect to the database")
#
# # cursor
# cur = conn.cursor()
#
# # execute query
# #cur.execute("insert into employers (id, name) values (%s, %s)", (7, "Akash"))
#
# cur.execute("Select id, name from employers")
# rows = cur.fetchall()
# emp_dict = {}
# emp_list = []
# for r in rows:
#     print(f"id {r[0]} name {r[1]}")
#     #print(f"{r[0]} {r[1]}")
#     emp_list.append(f"{r[0]} {r[1]}")
# print(emp_list)
# print(emp_list[3])
#
# # commit the transaction
# conn.commit()
# # close the cursor
# cur.close()
#
# # close the connection
# conn.close()

# import time
#
#
# def sleeper():
#     while True:
#         # Get user input
#         num = input('How long to wait: ')
#
#         # Try to convert it to a float
#         try:
#             num = float(num)
#         except ValueError:
#             print('Please enter in a number.\n')
#             continue
#
#         # Run our time.sleep() command,
#         # and show the before and after time
#         print('Before: %s' % time.ctime())
#         time.sleep(num)
#         print('After: %s\n' % time.ctime())
#
#
# try:
#     sleeper()
# except KeyboardInterrupt:
#     print('\n\nKeyboard exception received. Exiting.')
#     exit()

# import time
# print(time.time(), time.clock())

# import time
#
# start = time.time()
# print("hello")
# end = time.time()
# print(end - start)

# from datetime import datetime
#
# start_time = datetime.now()
#
# # INSERT YOUR CODE
#
# time_elapsed = datetime.now() - start_time
#
# print('Time elapsed (hh:mm:ss.ms) {}'.format(time_elapsed))

# x = 1
#
# i_cmd = 1
# while True:
#   s = input('Input [{0:d}] '.format(i_cmd))
#   i_cmd += 1
#   n = len(s)
#   if n > 0 and s.lower() == 'break'[0:n]:
#     break
#   exec(s)
#
# print('x = ', x)
# print('I am out of the loop.')


# from timeit import default_timer as timer
#
# class benchmark(object):
#
#     def __init__(self, msg, fmt="%0.3g"):
#         self.msg = msg
#         self.fmt = fmt
#
#     def __enter__(self):
#         self.start = timer()
#         return self
#
#     def __exit__(self, *args):
#         t = timer() - self.start
#         print(("%s : " + self.fmt + " seconds") % (self.msg, t))
#         self.time = t
#
# f = benchmark("pagla")
# print(f)

# for r in rows:
#     serial, name = [f"{r[0]}"], [f"{r[1]}"]
#     name = str(name)
#     emploey_dict[serial][name] = serial, name
    #print(f"id {r[0]} name {r[1]}")
    # emploey_list.append(f"{r[0]}")
    # for list in emploey_list:
    #     emploey_dict[list] = counter
    #     counter += 1
    #emploey_dict[f"{r[1]}"][f"{r[0]}"] = emploey_dict
#print(emploey_list)
#print(emploey_list[7])
#print(emploey_dict)

#print('datahead')
import psycopg2
import time


# ***** connect to the db *******
try:
    conn = psycopg2.connect("dbname='datahead' user='postgres' host='localhost' password='datahead'")
    #print('database connected')
except:
    print("I am unable to connect to the database")

# cursor
cur = conn.cursor()

# execute query
cur.execute("Select id, name from employers")
rows = cur.fetchall()

counter = 1
emploey_dict = {r[0]:r[1] for r in rows}
print(emploey_dict)

# close the cursor
cur.close()

# close the connection
conn.close()

#import time
import datetime
# employe in and out
in_time_employee_serial = int()
in_time_employee_name = ''

# in_time_employee
#from time import gmtime, strftime
currentDT = datetime.datetime.now()
in_employe = int(input("Which employee want to enter: "))
in_time_employee = currentDT.strftime("%a, %b %d, %Y") + ' ' + currentDT.strftime("%I:%M:%S %p")#strftime("%Y-%m-%d %H:%M:%S", gmtime())

#print(emploey_dict.values())
for key in emploey_dict.keys():
    if in_employe == key:
        print("Active:", emploey_dict[key], in_time_employee)
        in_time_employee_name = emploey_dict[key]
        with open('output.txt', mode='a+') as file_write_read:
            file_write_read.write("{} {} \n".format(in_time_employee_name, in_time_employee))


# currentDT = datetime.datetime.now()
#
# print ("Current Year is: %d" % currentDT.year)
# print ("Current Month is: %d" % currentDT.month)
# print ("Current Day is: %d" % currentDT.day)
# print ("Current Hour is: %d" % currentDT.hour)
# print ("Current Minute is: %d" % currentDT.minute)
# print ("Current Second is: %d" % currentDT.second)
# print ("Current Microsecond is: %d" % currentDT.microsecond)
#
# print (currentDT.strftime("%Y-%m-%d %H:%M:%S"))
# print (currentDT.strftime("%Y/%m/%d"))
# print (currentDT.strftime("%H:%M:%S"))
# print (currentDT.strftime("%I:%M:%S %p"))
# print (currentDT.strftime("%a, %b %d, %Y"))


# SECONDS_PER_MINUTE = 60
# SECONDS_PER_HOUR = 3600
# SECONDS_PER_DAY = 86400
#
# # Read the inputs from user
# seconds = int(input("Enter number of seconds: "))
#
# # Calculate the days, hours, minutes and seconds
# days = seconds / SECONDS_PER_DAY
# seconds = seconds % SECONDS_PER_DAY
#
# hours = seconds / SECONDS_PER_HOUR
# seconds = seconds % SECONDS_PER_HOUR
#
# minutes = seconds / SECONDS_PER_MINUTE
# seconds = seconds % SECONDS_PER_MINUTE
#
# # Display the result
# print("The duration is: ", "%d:%02d:%02d:%02d" % (days, hours, minutes, seconds))

# if in_time_employee_serial:
#     out_employe = int(input("Which employee want to go out: "))
#     print(in_time_employee_name, "out of Office Now")
# print(in_time_employee_serial)
# print(in_time_employee_name, "out of Office Now")

import atexit
from time import time, strftime, localtime
from datetime import timedelta

def secondsToStr(elapsed=None):
    if elapsed is None:
        return strftime("%Y-%m-%d %H:%M:%S", localtime())
    else:
        return str(timedelta(seconds=elapsed))

def log(s, elapsed=None):
    line = "="*40
    print(line)
    print(secondsToStr(), '-', s)
    if elapsed:
        print("Elapsed time:", elapsed)
    print(line)
    print()

def endlog():
    end = time()
    elapsed = end-start
    log("End Program", secondsToStr(elapsed))

start = time()
atexit.register(endlog)
log("Start Program")

