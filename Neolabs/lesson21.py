#assignment20
# def output(text): #funkcia prinimaet text i vyvodit vse s malenkogo
#     small = 0
#     big = 0
#     for letter in text: #prohodimsya po textu -> HoUse
#         if letter.islower(): #esli bukva malenkaia to schitaem
#             small += 1
#         else: #esli bolwaia to schitaem v drugoi peremennoi
#             big += 1
#     if small >= big: #v konce sravnivaem kol-vo raznyh bukv i vyvodim
#         print(text.lower())
#     else:
#         print(text.upper())
# output("HoUse")
# output("ViP")

# import lesson21test
# print(lesson21test.add(7,6))

# import math
# print("значение pi:", math.pi)
# print("значение e:", math.e)
# print(math.floor(3.99))
# print("значение cos:", math.cos(90))
import math
# import math as m #pereimenovali modul math as m
# print(m.e) #teper' rabotaet tolko s m
# print(m.pi) #staroe nazvanie ne rabotaet esli avtomaticheski ne importirovat'

# import lesson21test as l
# print(l.add(3,78)) #ne vazjno kakaia modul'

# from lesson21test import add #koroche chem vyweukazannyi metod
# print(add(1,45)) # pri zapuske nazvanie moduli ne piwetsia

# from math import pi, e, factorial, fabs #rabotaet tolko na pi
# print("значение pi:", pi) #nazvanie modulia mozhno
# print("значение e:", e) #ne rabotaet, potomu chto ne ukazan v 'from'
# print("значение factorial:", factorial(87))
# print("значение fabs:", fabs(67))


# from math import *
# print(pow(2,4))
# print(e)
# print(pi)

# import random
# com = random.randint(1,100) #sluchainoe chislo ot 1 do 100
# while True: #cikl igry
#     user = int(input("Угадайте число: ")) #popytka ugadat'
#     if com == user: #esli srazu ugadali
#         print("Вы угадали!")
#         break
#     elif com > user:
#         print("Слишком мало")
#     else:
#         print("Слишком много")


# import random
# moves = ["rock", "paper", "scissors"]
# com_win = 0
# user_win = 0
# while com_win != 3 and user_win != 3:
#     com = random.choice(moves)
#     user = input("введите выбор: ")
#     print(f"Компьютер выбрал {com}, вы выбрали {user}")
#     if com == "rock" and user == "scissors":
#         com_win += 1
#     elif com == "paper" and user == "rock":
#         com_win += 1
#     elif com == "scissors" and user == "paper":
#         com_win += 1
#
#     elif com == "rock" and user == "paper":
#         user_win += 1
#     elif com == "paper" and user == "scissors":
#         user_win += 1
#
#     print(f"Ком: {com_win}, пользователь: {user_win}")
#
# if user_win > com_win:
#     print("Пользователь пбедил!")
# else:
#     print("Компьтер победил!")
#
