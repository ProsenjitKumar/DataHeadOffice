my_data = [[100, 'Prosenjit Das', 'researcher', 'D1', '05:22:12', '01:10:48', 'P_Status'],
           [20, 'Arif Khan', 'Managing Director', 'D1', '12:25:11', '11:03:06', 'P_Status'],
           [13, 'Mr. hasib', 'Managing Director', 'D1', '05:25:19', '02:00:00', 'P_Status'],
           [1, 'Antu Sarkar', 'Engineer', 'D1', '08:15:54', '05:55:07', 'P_Status'],
           [50, 'Samoli Das', 'Engineer', 'D1', '05:16:54', '00:00:00', 'P_Status'],
           [10, 'Rupa Sarkar', 'Engineer', 'D1', '04:12:54', '03:55:07', 'P_Status']
           ]

import json
json_data = json.dumps(
    my_data
)

print(json_data)

# write json data.json
with open('data.json', mode='a') as write_data:
    write_data.write(str(json_data))
    write_data.write('\n')
    print("Data has written completely")

# read data.json
import storage
data = {}
storage.data['foo'] = 'bar'