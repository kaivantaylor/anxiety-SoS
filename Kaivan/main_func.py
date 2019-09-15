import csv
import datetime
from send_sms import message

sleep_list = []
heart_list = []
calorie_list = []

bool_sleep = False
bool_heart = False
bool_calorie = False

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

with open(r"C:\\Users\speedykai\Desktop\hophacks2019\Kaivan\CSV\sleep.csv") as csv_file:
    sleep = csv.reader(csv_file, delimiter=',')
    for row in sleep: # row is the addresses individually from the csv csv_file
        #print(row[2])
        try:
            b = int(row[2])
            sleep_list.append(b)
        except ValueError:
            pass
        if len(sleep_list) == 1:
            break
with open(r"C:\\Users\speedykai\Desktop\hophacks2019\Kaivan\CSV\calories.csv") as csv_file:
    calorie = csv.reader(csv_file, delimiter=',')
    for row in calorie: # row is the addresses individually from the csv csv_file
        try:
            c = int(row[0])
            calorie_list.append(c)
        except ValueError:
            pass

for heart_rate in heart_list:
    if heart_rate < 110:
        bool_heart = True

for sleep in sleep_list:
    if int(sleep) < 300:
        bool_sleep = True

cal_total = 0
for calorie in calorie_list:
    cal_total += calorie
#print(cal_total)
if cal_total < 1800:
    bool_calorie = True


total = 0
if bool_heart == True:
    total += 40
if bool_sleep == True:
    total += 40
if bool_calorie == True:
    total += 20

standard_msg = "Rendell's fitbit has detected abnormal metrics:" + "\n"
if bool_heart == True:
    ht_msg = 'Higher than usual heart rate (110+ BPM)' + "\n"
    standard_msg += ht_msg
if bool_sleep == True:
    sp_msg = 'Less than 5 hours of sleep' + "\n"
    standard_msg += sp_msg
if bool_calorie == True:
    cl_msg = 'Eating less than 1800 calories per day' + "\n"
    standard_msg += cl_msg

if total >= 60:
    message(standard_msg + "Please check on Rendell when you can.")
