import math
from random import randint
import time

s = " "
months = ["Poop", "Jan", "Feb", "March", "April", "May", "June", "July", "August", "Sep","Oct", "Nov", "Dec"]
thirty1 = ["Jan", "March", "May", "July", "August", "Oct", "Dec"]
centuryDay = [2, 7, 5, 3]
doomsDays = [20000000, 3, 28, 14, 4, 9, 6, 11, 8, 5, 10, 7, 12]

print("Give your answer in number of the day of the week:")
print("1 = Monday, 2 = Tuesday, 3 = Wednesday, 4 = Thursday, 5 = Friday, 6 = Saturday, 0 = Sunday")

year = 0
day = 0

times = []

while (s != "exit"):
    year = randint(1700,2050)
    if (year % 4 == 0):
        doomsDays[1] = 4
        doomsDays[2] = 29
    monthNo = randint(1,12)
    month = months[monthNo]
    found = False
    for i in range(7):
        if (month == thirty1[i]):
            found = True
            day = randint(1,31)
            break
    if (found == False):
        if (month == "Feb"):
            if (year % 4 == 0):
                day = randint(1,29)
            else:
                day = randint(1,28) % 28 + 1;
        else:
            day = randint(1,30)


    print("What is the day of the week on " + str(month) + " " + str(day) + ", " + str(year) + "?")
    time1 = time.time()

    century = centuryDay[(year // 100) % 4]
    doubleYear = (year % 100) % 28
    yearDoom = (((doubleYear+(doubleYear // 4)) % 7)+century) % 7
    ans = yearDoom

    if (day == doomsDays[monthNo]):
        ans += 0
    else:
        ans += day - (doomsDays[monthNo]%7)
    if (ans < 0):
        ans += 7

    ans = str(ans%7)
    while (1):
        s = input()
        if (s != ans):
            print("You are wrong. Try again.")
            print("Remember to give your answer in the form mentioned above.")
        else:
            time2 = time.time()
            duration = time2-time1
            times.append(duration)
            print("Yay! You got it in " + str(duration) + " seconds!")
            print("Current average: " + str(sum(times)/len(times)) + " seconds.")
            break
    doomsDays[1] = 3
    doomsDays[2] = 28
    print("Type any key to continue or 'stop' to stop")
    query = input()
    if (query == "next"):
        continue
    elif (query == "stop"):
        break