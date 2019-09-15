# Loops infinitely every 30-60 seconds
from update_CSV import update_CSV
from check_anxiety import check_anxiety
import sched, time

def run_loop():
    s = sched.scheduler(time.time, time.sleep)
    def do_something(sc):
        update_CSV()
        check_anxiety()
        standard_msg += ht_msg
        s.enter(35, 1, do_something, (sc,))

    s.enter(35, 1, do_something, (s,))
    s.run()


print("\n ---------------------------------------------------------------------------------------")
update_CSV()
check_anxiety()
run_loop()
