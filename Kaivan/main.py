import csv
import datetime
from send_sms import send_sms

heart_list = []
bool_heart = False
sleep_list = []
bool_sleep = False

with open(r"C:\\Users\speedykai\Desktop\hophacks2019\Kaivan\CSV\heartrate.csv") as csv_file:
    heart_rate = csv.reader(csv_file, delimiter=',')
    for row in heart_rate: # row is the addresses individually from the csv csv_file
        try:
            a = int(row[1])
            heart_list.append(a)
        except ValueError:
            pass
        if len(heart_list) == 10:
            break

for heart_rate in heart_list:
    if heart_rate < 110:
        bool_heart = True

with open(r"C:\\Users\speedykai\Desktop\hophacks2019\Kaivan\CSV\sleep.csv") as csv_file:
    sleep = csv.reader(csv_file, delimiter=',')
    for row in sleep: # row is the addresses individually from the csv csv_file
        print(row[2])
        try:
            b = row[2]
            sleep_list.append(b)
        except ValueError:
            pass
        if len(sleep_list) == 1:
            break
for sleep in sleep_list:
    if int(sleep) < 300:
        bool_sleep = True

total = 0
if bool_heart == True:
    total += 40
if bool_sleep == True:
    total += 40
