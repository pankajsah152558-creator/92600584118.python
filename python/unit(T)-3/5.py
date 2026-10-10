import datetime

now = datetime.datetime.now()

print("Current Date:", now.date())
print("Current Time:", now.strftime("%H:%M:%S"))
print("Current Date and Time:", now)
