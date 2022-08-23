# #buble sort - sravnivaet chisla i menyaet mestami a selection sort menyaet pozicii iwet samoe malenkoe  hislo
# swap = False
# while not swap:
#     print("hey")
#     swap = True #preryvaem cikl, menyaem peremennye chtoby prervat' cikl
#
#
# # example of insert sortirovka
#         # 0,1,2
# list = [1,3,5]
# list.insert(1, 2) #index-1, object - 2
# print(list)
#
#
# # quick sort vybiraet tochku opora i sravnivaet s drugimi chislami



# a = 5
# b = 10
#
# a, b = b, a
# print(a, b)
# # Json - Javascript Object Notation
# dict = {"name": "Alex", "age": 123"} # format peredachi dannyh


# # neeffektivno dlya bolwix spiskov
# list1 = ["Alex", "Vika", "Orhan", "Farrad"]
# name = input("vvedite imya ")
# # for i in range(len(list1)):
# #     if name == list1[i]:
# #         print(i) #poziciia v spiske
# # primer lineinogog sposoba poiska po imeni
# count = 0 # cherez while
# while count < len(list1):
#     if name == list1[count]:
#         print(count)
#     count += 1



# vtoroi sposob binarnyi poisk
# import random
# comp = random.randint(1, 100)
# while True:
#     user = int(input("ugadaite chislo: "))
#     if user == comp:
#         print("Vy ugadali!")
#         break
#     elif user > comp:
#         print("Sliwkom mnogo!")
#     elif user < comp:
#         print("sliwkom malo!")

# linear search - v hudwem sluchae 100 popytok esli sto elementov
# binary search - delit na dva; v hudwem sluchae 7 popytok esli tam 100 elementov, esli spisok ne otsortivrovan neeffectiven, rabotaet tolko esli spisok otsortirovan


# print(7//3) # dvoinye okruglyaet v menwuiu storonu
# print(7//-3)



# home = int(input("koordinaty doma: "))
# step = 0
# tile = 0
# while home > tile:
#     tile += 5
#     step += 1
# print(step)
# step1 = 0
# for tile in range(1, home+1, 5): # 1 - nachalo, home - konec, 5 - kletochek
#     step1 += 1 # +1 - 1 wag 5 kletochek - 1 wag
# print(step)




# nums = input().split() # prevrawaet v spisok i delit po probelu vnutri
# total = 0
# for element in nums: # prohodimsya po kajdomu chislu v spiske
#     total += int(element) # k summe dobavliaem chislo, int prevrawaet spisok v chislo
# print(total)


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def eat(self):
#         print("eat")
#     def sleep(self):
#         print("sleep")
# person1 = Person("Alex", "23")
# print(person1.name, person1.age)
# person1.eat()
# person1.sleep()


# def output(*element):
#     for i in element:
#         print(i, end=" ")
# output(5, 4, 78)