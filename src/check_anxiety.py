# Kaivan Taylor
# Creates an algorithm for determining the user's anxiety level. The algorithm uses
# an index level which is determined from three variables. That is the heart rate, calorie intake,
# and the amount of sleep from last night. Sleep and heart rate accounts for 40% of the index and
# calorie intake accounts for 20%.
#
# Contributers:
# Sleep is less than 5 hours
# Calorie intake is less than 1800 Calories
# Heart rate is more than 130 BPM

import csv
import datetime
from send_sms import message

def check_anxiety():
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
                if len(heart_list) == 10:
                    break
            except ValueError:
                pass

    with open(r"C:\\Users\speedykai\Desktop\hophacks2019\Kaivan\CSV\sleep.csv") as csv_file:
        sleep = csv.reader(csv_file, delimiter=',')
        for row in sleep: # row is the addresses individually from the csv csv_file
            #print(row[-1])
            try:
                b = int(row[1])
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
    print("----------------------------------------------------------------------")
    print(datetime.datetime.now().strftime("%Y%m%d"))
    print(datetime.datetime.now())
    for heart_rate in heart_list:
        print("Heart Rate:", heart_rate)
        if heart_rate > 130:
            bool_heart = True

    for sleep in sleep_list:
        print("Minutes Slept Last Night:", sleep)
        if int(sleep) < 300:
            bool_sleep = True

    cal_total = 0
    for food in calorie_list:
        cal_total += food
        print("Calories consumed:", food)
    print(cal_total)

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
        ht_msg = 'Higher than usual heart rate (130+ BPM)' + "\n"
        standard_msg += ht_msg
    if bool_sleep == True:
        sp_msg = 'Less than 5 hours of sleep' + "\n"
        standard_msg += sp_msg
    if bool_calorie == True:
        cl_msg = 'Eating less than 1800 calories per day' + "\n"
        standard_msg += cl_msg

    return total
