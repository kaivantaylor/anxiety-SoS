# Loops infinitely every 30 seconds
from update_CSV import update_heartrate
import sched, time

def infinite_update():
    update_heartrate()
    s = sched.scheduler(time.time, time.sleep)
    def do_something(sc):
        update_heartrate()
        s.enter(30, 1, do_something, (sc,))

    s.enter(30, 1, do_something, (s,))
    s.run()

    System.out.println("\n ------------------------------------------------")
