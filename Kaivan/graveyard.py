all_ten = True

hour = datetime.datetime.now().hour
minute = datetime.datetime.now().minute
secondminute = minute - 10
#print("second minute",secondminute)

if secondminute < 0: # If minute-10 is negative, go back one hour and give appropriate minute
    secondhour = hour - 1
    #print("secondhour",secondhour)
else:
    secondhour = hour

if secondhour and secondminute == -1: # 00:09:00 will base off of 00:00:00 instead of going into yesterday
    all_ten = False
    secondhour == 0
    secondminute == 0
    secondhour = str(secondhour)
    secondminute = str(secondminute)

count1 = minute - 1
count2 = minute - 2
count3 = minute - 3
count4 = minute - 4
count5 = minute - 5
count6 = minute - 6
count7 = minute - 7
count8 = minute - 8
count9 = minute - 9

def return_time(hour, minute):
    strhour = str(hour)
    strminute = str(minute)
    if len(strhour) == 1: # If it is less than 9, add 0 to make it compliant to military time
        hour = ("0" + str(hour))
    if len(strminute) == 1: # If it is less than 9, add 0 to make it compliant to military time
        minute = ("0" + str(minute))
    strhour = str(hour)
    strminute = str(minute)
    a = strhour + ':' + strminute + ":00"
    return a

if hour == secondhour:
    a = return_time(hour, minute) # current time 00:50:00
    b = return_time(hour, count1) # current time 00:49:00
    c = return_time(hour, count2) # current time 00:48:00
    d = return_time(hour, count3) # current time 00:47:00
    e = return_time(hour, count4) # current time 00:46:00
    f = return_time(hour, count5) # current time 00:45:00
    g = return_time(hour, count6) # current time 00:44:00
    h = return_time(hour, count7) # current time 00:43:00
    i = return_time(hour, count8) # current time 00:42:00
    j = return_time(hour, count9) # current time 00:41:00
    k = return_time(hour, secondminute) # current time 00:40:00

else: # current time 01:08:00
    if count1 < 0:
        count1 = 0
    if count2 < 0:
        count2 = 0
    if count3 < 0:
        count3 = 0
    if count4 < 0:
        count4 = 0
    if count5 < 0:
        count5 = 0
    if count6 < 0:
        count6 = 0
    if count7 < 0:
        count7 = 0
    if count8 < 0:
        count8 = 0
    if count9 < 0:
        count9 = 0
    if secondminute < 0:
        secondminute = 0
    a = return_time(hour, minute) # current time 01:08:00
    b = return_time(hour, count1) # current time 01:07:00
    c = return_time(hour, count2) # current time 01:06:00
    d = return_time(hour, count3) # current time 01:05:00
    e = return_time(hour, count4) # current time 01:04:00
    f = return_time(hour, count5) # current time 01:03:00
    g = return_time(hour, count6) # current time 01:02:00
    h = return_time(hour, count7) # current time 01:01:00
    i = return_time(hour, count8) # current time 01:00:00
    j = return_time(hour, count9) # current time 00:59:00
    k = return_time(hour, secondminute) # current time 00:58:00

timelist = []
timelist.append(a)
timelist.append(b)
timelist.append(c)
timelist.append(d)
timelist.append(e)
timelist.append(f)
timelist.append(g)
timelist.append(h)
timelist.append(i)
timelist.append(j)
timelist.append(k)

#print(timelist)
#print(type(timelist[0])) # string
