import time

my_data = [[100, 'Prosenjit Das', 'researcher', 'D1', '05:12:12', '01:10:48', 'P_Status'],
           [20, 'Arif Khan', 'Managing Director', 'D1', '12:15:51', '11:03:06', 'P_Status'],
           [13, 'Mr. hasib', 'Managing Director', 'D1', '05:15:49', '02:00:00', 'P_Status'],
           [1, 'Antu Sarkar', 'Engineer', 'D1', '08:45:54', '05:55:07', 'P_Status'],
           [50, 'Samoli Das', 'Engineer', 'D1', '05:12:54', '00:00:00', 'P_Status'],
           [10, 'Antu Sarkar', 'Engineer', 'D1', '06:12:54', '03:55:07', 'P_Status']
           ]

rep = [[50, 'Samoli Das', 'Engineer', 'D1', '05:12:54', '00:00:00', 'P_Status'],
       [13, 'Mr. hasib', 'Managing ', 'Director', 'D1', '05:15:49', '02:00:00', 'P_Status']]


changed = [['01:12:54'], ['05:12:54']]

with open('change.txt', 'w') as change:
    change.write(str(my_data))
    change.close()

with open('change.txt', mode='r') as pagla_value:
    for line in pagla_value:
        with open('change.txt', mode='w') as pagla1:
            for i, j in zip(rep, changed):
                pagla1.write(line.replace(str(i), str(j)))
            pagla1.close()

# import shutil, os
# shutil.copy2('change.txt', 'copy.txt')
#
# os.remove('copt.rxr')

current_time = time.localtime()
print(time.strftime('%H:%M:%S GMT', current_time))
