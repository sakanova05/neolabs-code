# #pervyi sposob
# my_dict = {"Kyrgyzstan": "Bishkek",
#            "UK": "London",
#            "Kazakhstan": "Nursultan",
#            "Russia": "Moscow"}
# for key in my_dict:
#     print(key, my_dict[key])
#
#

# # 2 sposob
# my_dict = {"Kyrgyzstan": "Bishkek",
#            "UK": "London",
#            "Kazakhstan": "Nursultan",
#            "Russia": "Moscow"}
# for key, value in my_dict.items():
#     print(key, value)
#

# my_dict = {"Kyrgyzstan": "Bishkek",
#            "UK": "London",
#            "Kazakhstan": "Nursultan",
#            "Russia": ["Moscow"], # kluchi izmenyautsya a znacheniya net
#            "Russia": "qwe"} # dublikaty nelzya hranit'
# print(my_dict.popitem()) # vuyveli s pomow'u pop poslednie kluch i znachenie



# JSON - Javascrip Object Notation - format dannyh

# #napishite function, kotoraia prinimaet 2 slova i pri vyvode ob'ediniaet ih
# # slojenie strok - конкатенация
# def concatination(first, second):
#     print(first+second)
# concatination("hello", "there")
#
#
# def output():
#     print(1)
#     print(2)
#     print(3)
#     return 4 # otpravliaet rezultat comp'uteru i vyhodit iz funkcii
#     print(5)
#     print(6)
# output()
#
#
#
# def check():
#     pass # funkcia v pythone vsegda vozvrawaet kakoe-to znachenie (None)
# print(check())


# def add(a,b):
#     """функция принимает два числа и выводит сумму""" # comment ne yavlyaetsya documentaciei
#     print(a + b)
# add(4, 6)
# print(add.__doc__) # vyzov stroki documentacii




# Napishite funkciu fullint(num), kotoraia prinimaet kakoi-to text
# chislo. I esli chislo yavlyaetsya negativnym to udaliaet znak minusa
# def fullint(num):
#     if num < 0:
#         print(-num)
#     else:
#         print(num)
# fullint(89)
# fullint(-90)


#
# def info(*args): # args yavlyaetsya tuple pri rabote s funkciei
#     print(type(args))
# info()
#
#
# def adder(*num):
#     total = 0
#     for i in num:
#         total += i
#     print(total)
# adder(1,2,3) # prinimaet neopredelennoe kol-vo chisel
# adder(123,345,57)
# adder(123,23,346,23,234,1234,123,234,345,34,5,234,234,234)
# adder() # mojno ostavit' pustoi
#
#
#
# def info(**kwargs): # kwargs - yavlyaetsya slovarem
#     for key, value in kwargs.items():
#         print(key, value) # esli est' end = " ", to pokajet v strochku
# info(name = "Alex", surname = "Farrad")


# def my_fun(*args, **kwargs): # mojno ob'edinit' oba parametra
#     print(args)
#     print(kwargs)
# my_fun(1,2,3, name = "Vika", age = 123)


# Kogda funkciia vyzyvaet samu sebya eto rekursiia

# random - standartnyi modul'
# import random # modul mozhno predskazat', ne stoit ispol'zovat' dlya deistvitel'no vajnyh vewei
# print(random.randint(1,5))


# # pol'zovatel'skii modul' - modul' napisannyi samim soboi
# print("hi")
# if __name__== "__main__": # kod zarabotaet pri zapuske iz original'nogo
#     print("hiya")
#


# import assignment23
# from assignment23 import * # zvezdochkalya togo chtoby ne poimat' pohojuiu
# from random import randint as r # importirovat' funkciu randint
# print(r(1,6)) # sluchainoe chislo s 1 do 6



# exceptions ispol'zutsya s try i except
# try:
#     print("na nol' delit' nel'zya")
# except ZeroDivisionError: # esli v kode est' owibka, to zarabotaet block except
#     print("na nol' delit' nel'zya")
#
#
# try:
#     num = int(input())
#     if num < 0:
#         raise ValueError()

# pochitat' nameError, ValueError,

#
# x = 10
# def fun():
#     print(x)
# x = 10 # doljno stoyat' pered vyzovom
# fun()


# x = 10 # global'naya peremennaia
# def fun():
#     x = 20 # lokal'naia peremennaia
#     print(x)
# fun() # pokajet 20
# print(x) # pokajet 10



# y = 0
# def total():
#     global y # pri izmenenii nujen global dlya poiska peremennoi
#     y = y + 1
#     print(y)



# Sozdaite class Jet (samolet), kotoryi imeet 2 atributa,
# i 2 metoda
# class Jet:
#     def __init__(self, name, color): # svoistva atributy
#         self.name = name
#         self.color = color
#
# def take_off(self): # metody-povedenie
#     print("airplane takes off")
#
# def land(self):
#     print("airplane lands")
#
# F14 = Jet("f14", "pink")
# print(F14.name, F14.color)

