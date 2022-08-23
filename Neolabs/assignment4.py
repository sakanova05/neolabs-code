x = 12
y = 6
percentage = y/x * 100
print(percentage)
percentage = int(input("допуск к экзамену"))
if percentage <= 75:
    print("допущен")
elif percentage <= 55 or percentage > 35:
    print("не допущен")