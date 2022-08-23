# print (*my_list, sep="\n") = srazu v stolbik spisok
# znachenie "if"
# if (8 > 5):
#     print(bytes)
# if "sit" < "see":
#     print("bye")
#
# num1 = input("eat")
# print(type (num1))

# num1 = int(input("insert number")) #prinimaet ot client
# num2 = int(input("insert second number"))
# if num1 > num2:
#     print("sleep")
# elif num1 > num2:
#     print("go")
# else:
#     print("go")

# if 9 > 8:
    # print("pass") propuskaet

# if 10 > 8 and 10 > 9: # oba usloviya doljzhy byt' vypolneny
#     print("go away")
# if 15 > 10 or 10 > 15: #odnogo dostatochno
#     print("drink")

# day = int(input("insert day "))
# monday = (5, 6, 7)
# tuesday = (1, 4, 2)
# wednesday = (9, 3, 8)
# thursday = (10, 11, 12)
# if day in monday: #check on existence and 'else' will work too with 'if' but with 'elif' 'else' won't work thus 'elif' is better
#     print("dunkin donuts")
# if day in tuesday:
#     print("dance")
# if day in wednesday:
#     print("stand")
# else:
#     print("net takix dnei")

# num = "1.5"
# num = float(num) - vewestvennoe chislo

seasons = int(input("sit"))
summer = (8, 9, 10)
spring = (11, 12,13)
winter = (14, 15, 16)
if seasons >= 1 and seasons <= 2 or seasons==12:
    print ("winter")
elif seasons >=3 or seasons <= 5:
    print("spring")
else:
    print ("does not exist")