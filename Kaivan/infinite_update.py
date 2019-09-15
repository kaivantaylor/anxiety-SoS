# Loops infinitely every 30 seconds
from update_CSV import update_CSV
from main_func import check_anxiety
import sched, time

def infinite_update():
    update_CSV()
    check_anxiety()
    s = sched.scheduler(time.time, time.sleep)
    def do_something(sc):
        update_CSV()
        standard_msg += ht_msg
        s.enter(30, 1, do_something, (sc,))

    s.enter(30, 1, do_something, (s,))
    s.run()

    System.out.println("\n ------------------------------------------------")

infinite_update()
