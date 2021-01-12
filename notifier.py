from win10toast import ToastNotifier
from datetime import datetime
import time


def get_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    current_seconds = now.strftime("%S")
    return [current_time, current_seconds]


if __name__ == '__main__':
    init = 0
    while True:
        if get_time()[1] == "00" or init == 1:
            time.sleep(5)
            init = 1
        else:
            time.sleep(1)
        if get_time()[0] == "23:32:00":
            toaster = ToastNotifier()
            toaster.show_toast("notifier summary", "notifier description",icon_path="icon_path",duration=10)
            
