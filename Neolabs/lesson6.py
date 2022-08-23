# text = "hello"
# for letter in text:
#     print(letter * 2, end = "-")
#
# my_list = ["eat","drink", "dance"]
# count = 0
# while count < len(my_list):
#     print(my_list[count])
#     count += 1
#
# my_list = ["eat", "drink", "dance"]
# for task in my_list:
    # print(task) task eto peremennaia and you can change to other words

# my_list = ["eat", "drink", "dance"] #prowlis' po slovu - po bukvam
# text = "eat"
# for letter in text:
#     print(letter)
#
# for num in range(1, 11): # 1 do 10 not included 11, range is function which goes only in a positive way ex, 1-10 but not 10-1
#      print(num)
#
# for num in range(10, 0, -1): # a - nachalo, b - end, c - wag
#     print(num)
#
# for num in range(1, 11, 2):
#     print(num)

# total = 0 # summa 0
# n = 5 # the end - do kuda schitaetsia
# for i in range(1, n + 1): #dlya chisla s 1 do 5, vmesto i mozhno luboe slovo ili bukvu
#    total += i #poschitwlivsummu
#    print(total)

# start = int(input("vvedite nachalo: "))
# end = int(input("vvedite konec: "))
# step = int(input("vvedite skol'ko wagov propustit': "))
# for element in range(start, end+1, step):
#     print(element)

# for num in range(20, 30+1):
#     print(num)


# for letter in "hello world": #prohodimsia po stroke
#     if letter == " ": #esli stroka stala probelom
#         break # vyhodim iz cikla
#     print(letter)

# while True: # cikl, prodolzhaetsia
#     print("hey")
#     break # razbivaet cikl
#


# for letter in "hellow world":
#     if letter == "o":
#         continue # propuskaet tolko bukvu no prodolzhaet delat' komandu v otlichiiot "break" and "pass"(ignor)
#     print(letter, end=" ") # end= chtoby bylo krasivo gorizontal'no
#
# print(1, 2, 3, sep = "\n", end = ".") # sep = separator kotpryi budet dobavlyat' chto ukazano separatorom mezhdu peremennymi
# print(4, 5, 6)

#
# my_list = []
# for num in range(1, 6):
#     my_list.append(num)
# print(my_list) #vyveli chisla ot 1 do 5 ispolzuia tolko diapazon

# my_list = [] #menyali kod tak, chto vmesto chisel s 1 do 5(primer vywe) dobavliautsia slova kotorye my prinimaem ot polzovatelia
# for word in range(1,6): # 6 deistvii, range - eto diapazon vsegda idet s ciframi a ne slovami
#     user = input("actions: ") # chtoby prinimat' ot polzovatelia - input
#     my_list.append(user) # dobavliatsia userom - komanda append
# print(my_list) #vyvodit, eto zameniat programmu s while



