# class Person:
#     def breath(self):
#         print("chelovek dywit")
#
# class Doctor(Person): # nasledovanie - snachala smotrit na method potom u kakogo roditelya unasledovano
#     def cure(self): # extending - raswirenie, mu raswirili sposobnosti doctora
#         print("doctor lechit")
#
#     def breath(self): # overriding - perezapis'
#             print("doctor ne sovsem dywit")
#
# doctor1 = Doctor()
# doctor1.cure()
# doctor1.breath()



# OOP - Obkect oriented programming, obektno orientirovannoe programmirovanie

# class Bank:
#     def __init__(self):
#         self.__money = 1000 #incapsulyacia
#
#     def getMoney (self): # s pomow'u funkcii vyveli incapsulliaciu/zawiwennyi attribute, getter dlya zaprosa info
#         return self.__money
#
#     def setMoney (self, money): # setter dlya izmenenia info
#         self.__money = money
#
#
#
# person1 = Bank()
# print(person1.getMoney()) # poluchili balans
# person1.setMoney(2000) # pomenyali balans
# print(person1.getMoney()) # uznali novyi balance

# class Phone:
#     def __init__(self):
#         self._price = 3000
#
# Nokia = Phone()
# print(Nokia._price)

# __ = private attribute, tut spec metod
# _ = protected attribute, a zdes vydaet preduprezhdenie i napryamui obtatitsya


# class Dog:
#     def voice(self): #polyphormism
#         print("Woof woof!")
#
# class Cat:
#     def voice(self):
#         print("Meow meow!")
#
# dog1 = Dog()
# cat1 = Cat()
# animals = [dog1, cat1]
# for pet in animals:
#     # if isinstance(pet, Dog):
#     #     pet.dog_voice()
#     # elif isinstance(pet, Cat):
#     #     pet.cat_voice()
#     pet.voice()


#another example of polyphormism
# class Parrot:
#     def swim(self):
#         print("Parrot can't swim")
#
# class Penguin:
#     def swim(self):
#         print("Penguin can swim")
#
# def swimming_test(bird):
#     bird.swim()
#
#
# red = Parrot() # red = ob'ekt
# black = Penguin()
# swimming_test(red) # ukazali ob'ekt
# swimming_test(black)




#lesson28 - files


# file = open("test.txt", encoding="utf-8") # encoding - pokazyvaet vse yazyki
# print(file.read())
# file.close()
# print("hey\nthere") # razdelyaet - n
#
# file = open("test.txt", "w", encoding="utf-8") # encoding - pokazyvaet vse yazyki
# print(file.write("red")) # perezapisyvaet i udalyaet vse chto bylo
# file.close()

#specifying full path - f = open(r"specfic path") - second method

# RAM - energozavisim i na korotkoe hranenie
# jestkii disk (ssd/hdd) - enrgoNEzavisimoe hranenie

# file = open("test.txt", "r", encoding="utf-8")
# print(file.read(2))
# print(file.read(2))
# print(file.read(2))
# print(file.tell()) # pokazyvaet poziciu kursora - v danno sluchae 6
# file.seek(10) # seek - eto perenos kursora na poziciu
# print(file.read())
# file.close()


# odin iz bezopasnyh sposobov zakryt' file
# try:
#     file = open("test.txt", "r", encoding="utf-8")
#     print(1/0)
# except:
#     pass
# finally:
#     file.close()


# samyi bezopasnyi metod dlya zakrytiia
# with open("test.txt", "r", encoding="utf-8") as file:
#     print(file.read())

# with open("test.txt", "w", encoding="utf-8") as file:
#     file.write("flower\n") # n nujen dlya razdelenia chtoby ne v odnoi stroke byli files
#     file.write("romashka")



# with open("test.txt", "w", encoding= "utf-8") as file:
#     for num in range(1, 101): # vyhodit v file test.txt
#       file.write(f"{num}\n") # otfomotirovali cchtoby pokazalo cifry i n dlya stolbika



# with open("test.txt", "r", encoding= "utf-8") as file:
#     text = input("vvedite text: ")
#     for word in file.read().split():
#         if word in text:
#             text = text.replace(word, "*" * len(word)) # naprimer mojno napisat' programmu kotoraia zamenyaet maty
#     print(text)


# with open("test.txt", "r", encoding= "utf-8") as file:
#     text = input("vvedite text: ")
#     for word in file.read().split():
#         if word in text:
#             print("takoi parol' suwestvuet")



