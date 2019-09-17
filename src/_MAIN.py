# Kaivan Taylor
# This file runs a loop every 35 seconds which will first fetch from the fitbit server
# and parse the JSON for data which will be saved into a CSV folder.
# From the CSV, the algorithm in check_anxiety will determine whether or not the user's
# level of anxiety is high enough. If so, it will send a message through twillo API

from update_CSV import update_CSV # importing other .py files functions
from check_anxiety import check_anxiety
import sched, time # time tracking

def run_loop():
    loop_seconds = 35 # one variable to make it easier to change the time
    s = sched.scheduler(time.time, time.sleep)
    def do_something(sc):
        update_CSV()
        check_anxiety()
        s.enter(loop_seconds, 1, do_something, (sc,))

    s.enter(loop_seconds, 1, do_something, (s,))
    s.run()


print("\n ---------------------------------------------------------------------------------------")
update_CSV()
check_anxiety()
run_loop()
