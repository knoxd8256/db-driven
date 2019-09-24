def printRain():
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    rain = [1, 2, 3, 4, 5, 6, 7]
    for day in rain:
        print(weekdays[day-1], rain[day-1])