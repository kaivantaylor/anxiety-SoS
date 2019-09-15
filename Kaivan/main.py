import csv
import datetime
from send_sms import send_sms

list_stop = []

with open(r"C:\\Users\speedykai\Desktop\hophacks2019\Kaivan\CSV\heartrate.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader: # row is the addresses individually from the csv csv_file
        try:
            a = int(row[1])
            list_stop.append(a)
        except ValueError:
            pass
        if len(list_stop) == 10:
            break

for heart_rate in list_stop:
    if heart_rate < 90:
        send_sms()
    else:
        pass
