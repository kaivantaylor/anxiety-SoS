# Kaivan Taylor
# This file runs a loop every 35 seconds which will first fetch from the fitbit server
# and parse the JSON for data which will be saved into a CSV folder.
# From the CSV, the algorithm in check_anxiety will determine whether or not the user's
# level of anxiety is high enough. If so, it will send a message through twillo API

from update_CSV import update_CSV # importing other .py files functions
from get_Anxietyindex import get_Anxietyindex
from secret import elijsha,rendell,kaivan,twillonumber
import sched, time # time tracking

def run_loop():
    loop_seconds = 35 # one variable to make it easier to change the time
    s = sched.scheduler(time.time, time.sleep)

    def do_something(sc): #loop every "loop_seconds" seconds
        update_CSV() # Update CSV to get latest data

        index_msg = get_Anxietyindex() # Get index and msg from check_anxiety()
        if index_msg[0] >= 60: # Check to see if index is high enough to send messge
            str_msg = str(index_msg[1] + "Please check on Rendell immediately.")
            #message(str_msg, elijsha)
            message(str_msg, kaivan)

        s.enter(loop_seconds, 1, do_something, (sc,))

    s.enter(loop_seconds, 1, do_something, (s,))
    s.run()

print("\n ---------------------------------------------------------------------------------------")
run_loop()
