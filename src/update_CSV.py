# Source: https://towardsdatascience.com/collect-your-own-fitbit-data-with-python-ff145fa10873
# Getting familiar with fitbit API
# Kaivan Taylor
#
# This program sends an HTTPS request from fitbit servers which returns a JSON. The JSON
# is then converted to a CSV format and updates the folder.

import fitbit # Fitbit API
import gather_keys_oauth2 as Oauth2 # Oauth2 used for authorizing server
import pandas as pd # Pandas used for data frame
import datetime # date time for date which makes it easier to get date instead of typing it out
import os # os for deleting files and changing working directory
from secret import fb_CLIENT_ID,fb_CLIENT_SECRET # for hiding phone numbers and client ids

CLIENT_ID = fb_CLIENT_ID
CLIENT_SECRET = fb_CLIENT_SECRET

def update_CSV():
    server = Oauth2.OAuth2Server(CLIENT_ID, CLIENT_SECRET)
    server.browser_authorize() # Using token to authenticate server
    ACCESS_TOKEN = str(server.fitbit.client.session.token['access_token'])
    REFRESH_TOKEN = str(server.fitbit.client.session.token['refresh_token'])
    auth2_client = fitbit.Fitbit(CLIENT_ID, CLIENT_SECRET, oauth2=True, access_token=ACCESS_TOKEN, refresh_token=REFRESH_TOKEN)

    yesterday = str((datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y%m%d")) # today - 1 day
    yesterday2 = str((datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%m-%d")) # today - 2 days
    today = str(datetime.datetime.now().strftime("%Y%m%d")) # today

    fit_heartrate = auth2_client.intraday_time_series('activities/heart', base_date='today', detail_level='1min') # retrieving JSON
    try:
        fit_sleep = auth2_client.sleep(date='today')['sleep'][0]
    except IndexError:
        fit_sleep = auth2_client.sleep(date=yesterday)['sleep'][0]
        fit_sleep = auth2_client.sleep(date=yesterday2)['sleep'][0]
    fit_calorie = auth2_client.recent_foods(user_id = "-")

    # Getting data from calories into a data frame
    a_list = []
    for i in fit_calorie:
        #print(i['calories'])
        a_list.append(i['calories'])

    caloriesdf = pd.DataFrame({'Calories':a_list})

    # Getting data from heart rate into data frame
    stime_list = []
    sval_list = []
    for i in fit_heartrate['activities-heart-intraday']['dataset']:
        stime_list.append(i['time'])
        sval_list.append(i['value'])
    stime_list.reverse()
    sval_list.reverse()
    heartdf = pd.DataFrame({'Heart Rate':sval_list,
                         'Time':stime_list})

    # Getting data from sleep into data frame
    sleepdf = pd.DataFrame({'Date':fit_sleep['dateOfSleep'],
                         'Efficiency':fit_sleep['efficiency'],
                         'Minutes Asleep':fit_sleep['minutesAsleep'],
                         'Time in Bed':fit_sleep['timeInBed']
                        },index=[0])

    # Changing working directory to correct folder
    #print(os.getcwd())
    #os.chdir("C:/Users/speedykai/Desktop/hophacks2019/docs")
    os.chdir("C:/Users/kaiva/Onedrive/Desktop/Programming/hophacks2019/docs")

    try: # deleting onld csv files to prevent overwriting in the same csv
        os.remove("calories.csv")
        os.remove("heartrate.csv")
        os.remove("sleep.csv")
    except FileNotFoundError:
        pass

    # Turning heart rate, sleep, and calorie dataframe into csv
    heartdf.to_csv('heartrate.csv',\
                   columns=['Time','Heart Rate'], header=True, \
                   index = False)
    sleepdf.to_csv('sleep.csv',\
                    columns=['Date','Efficiency','Minutes Asleep','Time in Bed'],\
                    header=True, index=False, mode = 'a')
    caloriesdf.to_csv('calories.csv',\
                        columns=['Calories'], header=True, index=False, mode = 'a')
