# my_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# for task in my_list:
#     print(task)
# for i in my_list:
#     if i % 2 == 0:
#         print(i, "четное")
#     else:
#         print(i, "нечетное")

# my_list = []
# for num in range(1, 16): # dlya chisel cs 1 do 15
#     my_list.append(num) # dobavliaem chisla v spisok
# print(my_list)
# # 2 part
# for element in my_list: #prohodimsia po spisku
#     if element % 2 == 1: # esli chislo nechetnoe
#         print(element * 3, end = " ")



# # example from codeforces
# weight = int(input("Введите час: "))
# if weight % 2 == 0 and weight != 2:
#     print("YES")
# else:
#     print("NO")


# my_str = "localization"# vyveli poslednuu bukvu
# print(my_str[-1])



# first letter - length of elements between - last letter

# my_str = input("vvedite: ") # program which accepts a word
# if len(my_str) > 10:# if a word is more than 10 elements
#     print(my_str[0], len(my_str)-2, my_str[-1], sep="") # first letter - length of elements between - last letter

# user = int(input()) # peremennaia dlya togo chtoby user sam vybiral skol'ko raz s pomow'u int input - celoe chislo vvodit'
# for i in range(user): # snachala cikl potom str, input dolzhen byt' vnutri cikla
#     my_str = input() # prinial slovo, ne piwi slovo kak peremennaia. napisat' nuzhno kak client
#     if len(my_str) > 10: # proveril kol-vo bukv
#         print(my_str[0], len(my_str) - 2, my_str[-1], sep="")



# while True: # poka pravil'no
#     password = int(input()) # prinimaet parol' poka pravilnyi
#     if password != 2016: # esli ne raven 2016
#         print("Incorrect password")
#     else: #inache
#         print ("Access permitted")
#         break # vyhodim iz cikla chtoby ewe raz ne sprawival parol' kogda vveli pravil'no

# second vesrion of the program with password - 2016

# password = int(input())
# while password != 2016:
#     print("incorrect password")
#     password = int(input())
#
# if password == 2016:
#     print("access permitted")

# zadacha pro svetodiody
# count = 0
# num = input("На какой год сколько украшений необходимо? ") # 115
# for i in num:
#     if i == "1":
#         count += 2
#     elif i == "2":
#         count += 5
#     elif i == "3":
#         count += 5
#     elif i == "4":
#         count += 4
#     elif i == 5:
#         count += 5
#     elif i == 6 or i == "9" or i =="0":
#         count += 6
#     elif i == 7:
#         count += 3
#     elif i == 8:
#         count += 7
# print("необходимо", count, "светодиодов")
