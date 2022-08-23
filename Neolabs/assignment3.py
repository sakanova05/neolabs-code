calendar_day = int(input("введите день: "))
night = (1, 2, 3, 4)
morning = (5, 6, 7, 8, 9, 10, 11)
day = (12, 13, 14, 15, 16, 17)
evening = (18, 19, 20, 21, 22, 23, 24)
if calendar_day <= 4 and calendar_day >= 3 or calendar_day ==2:
    print("night")
elif calendar_day <= 11 and calendar_day >= 7 or calendar_day >= 8:
    print("morning")
elif calendar_day >= 15 and calendar_day <= 17 or calendar_day >= 16:
    print("day")
elif calendar_day <= 24 and calendar_day >= 19 or calendar_day >= 22:
    print("evening") 