from plyer import notification
import time

while True:
	notification.notify(
		title= "**Please drink water now!**",
		message= "Drinking water is important for health",
		timeout= 10
		)
	time.sleep(60*60)
	break