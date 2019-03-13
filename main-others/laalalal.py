# from datetime import datetime, timedelta
# start = '10:00:00'
# end = '12:05:00'
# FMT = '%H:%M:%S'
# interval_time = datetime.strptime(end, FMT) - datetime.strptime(start, FMT)
# print(interval_time)
#
# if interval_time.days < 0:
#     tdiff = timedelta(days=0,
#                       seconds=interval_time.seconds, microseconds=interval_time.microseconds)
#     print(tdiff)

#
# import calendar
# # Create a plain text calendar
# c = calendar.TextCalendar(calendar.THURSDAY)
# str = c.formatmonth(2025, 1, 0, 0)
# print(str)
#
# # Create an HTML formatted calendar
# hc = calendar.HTMLCalendar(calendar.THURSDAY)
# str = hc.formatmonth(2025, 1)
# print(str)
# # loop over the days of a month
# # zeroes indicate that the day of the week is in a next month or overlapping month
# for i in c.itermonthdays(2025, 4):
#     print(i)
#
#     # The calendar can give info based on local such a names of days and months (full and abbreviated forms)
#     for name in calendar.month_name:
#         print(name)
#         for day in calendar.day_name:
#             print(day)
#     # calculate days based on a rule: For instance an audit day on the second Monday of every month
#     # Figure out what days that would be for each month, we can use the script as shown here
#         for month in range(1, 13):
#             # It retrieves a list of weeks that represent the month
#             mycal = calendar.monthcalendar(2025, month)
#             # The first MONDAY has to be within the first two weeks
#             week1 = mycal[1]
#             week2 = mycal[2]
#             if week1[calendar.MONDAY] != 0:
#                 auditday = week1[calendar.MONDAY]
#             else:
#             # if the first MONDAY isn't in the first week, it must be in the second week
#             auditday = week2[calendar.MONDAY]
#                 print("%10s %2d" % (calendar.month_name[month], auditday))

# import datetime
#
# now = datetime.datetime.now()
# print(now.strftime("%H:%M:%S"))


# date = 5
# history = [1,2,3,5,3,5,6,5,3,4,456,0,3,'none']
# history1 = ['none',1,2,3,5,3,5,6,3,4,456,0,3]
#
#
# latest_history = []
#
# for h in history1:
#     # print("id",h[0])
#     # if h[0] == 18:
#     #     print("date:", h[2])
#     #     print("last Dat:", last_log_date)
#     #     print("last Dat:", date_now)
#     # history_last_date = h[2]
#     #
#     if h == date:
#         print("soman")
#         latest_history.append(h)
# print(latest_history)

# history = [
#        [1, 'Prosenjit Das', None, None, None, None, None, None, None, None, 'Prosenjit Das'],
#        [2, 'Linda', datetime.date(2019, 3, 6), datetime.time(17, 50, 18), datetime.time(12, 50, 23), datetime.time(11, 30, 26), datetime.time(1, 19, 57), None, None, 1, None],
#        [4, 'Sudipto Rahman', datetime.date(2019, 3, 6), datetime.time(20, 56, 36), datetime.time(23, 56, 37), datetime.time(20, 24, 38), datetime.time(3, 31, 59), None, None, 1, None],
#        [5, 'Phan Tran', None, None, None, None, None, None, None, None, 'Phan Tran'],
#        [6, 'Ely Tran', datetime.date(2019, 3, 7), datetime.time(15, 4, 32), datetime.time(15, 39, 37), datetime.time(15, 4, 35), datetime.time(0, 35, 2), None, None, 1, None],
#        [7, 'Anna', datetime.date(2019, 3, 7), datetime.time(15, 34, 37), None, None, None, None, None, None, None],
#        [9, 'Arif', datetime.date(2019, 3, 7), datetime.time(19, 32, 50), datetime.time(20, 53, 15), datetime.time(20, 33), datetime.time(0, 20, 15), None, None, 1, None],
#        [3, 'Engineering', datetime.date(2019, 3, 8), datetime.time(10, 49, 58), datetime.time(12, 49, 59), datetime.time(11, 20), datetime.time(1, 29, 59), None, None, 1, None],
#        [10, 'Natalia', datetime.date(2019, 3, 9), datetime.time(13, 35, 20), None, None, None, None, None, None, None], [11, 'Olga', datetime.date(2019, 3, 9), datetime.time(13, 37, 47), None, None, None, None, None, None, None],
#        [12, 'Elena', datetime.date(2019, 3, 9), datetime.time(13, 38, 3), None, None, None, None, None, None, None],
#        [13, 'Sofia', None, None, None, None, None, None, None, None, 'Sofia'],
#        [14, 'Victoria', datetime.date(2019, 3, 9), datetime.time(13, 38, 35), None, datetime.time(13, 38, 36), None, None, None, None, None],
#        [19, 'Prosenjit Das', datetime.date(2019, 3, 10), datetime.time(11, 25, 43), None, None, None, None, None, None, None],
#        [18, 'Prosenjit Das', datetime.date(2019, 3, 10), datetime.time(11, 4, 25), None, None, None, None, None, None, None],
#        [8, 'Julia', datetime.date(2019, 3, 7), datetime.time(18, 59, 12), datetime.time(14, 11, 26), datetime.time(13, 57, 55), datetime.time(0, 13, 31), None, None, 1, None],
#        [15, 'Marina', datetime.date(2019, 3, 9), datetime.time(13, 59, 39), None, datetime.time(13, 59, 40), None, None, None, None, None],
#        [16, 'Smith', datetime.date(2019, 3, 9), datetime.time(13, 59, 58), None, datetime.time(13, 59, 58), None, None, None, None, None],
#        [17, 'Nazrul Islam', None, None, None, None, None, None, None, None, 'Nazrul Islam']
# ]
# print(history)


from datetime import datetime
#
# now = datetime.now()
# date_now = now.strftime("%Y-%m-%d")
# import datetime
# history = [
#        [1, 'Prosenjit Das', None, None],
#        [2, 'Linda', datetime.date(2019, 3, 6), datetime.time(17, 50, 18)],
#        [4, 'Sudipto Rahman', datetime.date(2019, 3, 6), datetime.time(20, 56, 36)],
#        [5, 'Phan Tran', None, None, None, None, None, None, None, None, 'Phan Tran'],
#        [6, 'Ely Tran', datetime.date(2019, 3, 7), datetime.time(15, 4, 32)],
#        [7, 'Anna', datetime.date(2019, 3, 7), datetime.time(15, 34, 37)],
#        [9, 'Arif', datetime.date(2019, 3, 7), datetime.time(19, 32, 50)],
#        [3, 'Engineering', datetime.date(2019, 3, 8), datetime.time(10, 49, 58)],
#        [10, 'Natalia', datetime.date(2019, 3, 9), datetime.time(13, 35, 20)],
#        [11, 'Olga', datetime.date(2019, 3, 9), datetime.time(13, 37, 47)],
#        [12, 'Elena', datetime.date(2019, 3, 9), datetime.time(13, 38, 3)],
#        [13, 'Sofia', None, None],
#        [14, 'Victoria', datetime.date(2019, 3, 9), datetime.time(13, 38, 35)],
#        [19, 'Prosenjit Das', datetime.date(2019, 3, 10), datetime.time(11, 25, 43)],
#        [18, 'Prosenjit Das', datetime.date(2019, 3, 10), datetime.time(11, 4, 25)],
#        [8, 'Julia', datetime.date(2019, 3, 7), datetime.time(18, 59, 12)],
#        [15, 'Marina', datetime.date(2019, 3, 9), datetime.time(13, 59, 39)],
#        [16, 'Smith', datetime.date(2019, 3, 9), datetime.time(13, 59, 58)],
#        [17, 'Nazrul Islam', None, None]
# ]
# #print(history)
# latest_history = []
# for h in history:
#     history_last_date = h[2]
#     if str(history_last_date) == str(date_now):
#         latest_history.append(h[0])
#         print("id", h[0], history_last_date, "!=", date_now)
#     # else:
#     #     print("id", h[0],history_last_date,"!=",date_now)
# print(latest_history,'\n')

# import pytz
#
# tz = pytz.timezone('Europe/Berlin')
# berlin_now = datetime.now(tz)
# print(berlin_now)
#
# from tzlocal import get_localzone
# local = get_localzone()
#
# from datetime import datetime
# print(datetime.now(local))


now = datetime.now()
#date_string = '2009-11-29 03:17 PM'
time_now = now.strftime("%H:%M:%S %p")
format = '%H:%M:%S %p'
my_date = datetime.strptime(time_now, format)

# This prints '2009-11-29 03:17 AM'
print(my_date.strftime(format))