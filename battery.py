import psutil
import time
from winotify import Notification

notified = False

while True:
    battery = psutil.sensors_battery()

    percent = battery.percent
    plugged = battery.power_plugged

    print(f"Battery: {percent}%  | Charger: {plugged}")

    if percent <= 30 and not plugged:

        if not notified:
            notification = Notification(
                app_id= "Battery Monitor",
                title="Battery Low",
                msg=f"{percent}% Batery remaining"
            )

            notification.show()
            notified = True
    else:
        notified = False

    time.sleep(60)