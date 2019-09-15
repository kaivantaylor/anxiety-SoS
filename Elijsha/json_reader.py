import json
import os
import requests

yes = requests.get('https://github.com/speedykai/hophacks2019/blob/master/Elijsha/heartrate_day1.json').json()
# os.chdir(r'C:\Users\speedykai\Desktop\hophacks2019\Elijsha')
# print(os.getcwd())
#
# yes = open("sleep_day1.json", 'r')
#
# with yes as read_file:
#     data = json.loads(read_file)
