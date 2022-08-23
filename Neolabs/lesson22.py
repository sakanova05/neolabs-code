#Types of errors
# print(5+"3") #TypeError
# print(1/0) #ZeroDivisionError
# print(a) #NameError
# print([1,2,3][99]) IndexError
# print({}["name"]) #KeyError


#
# try:
#     # print(5 + "3")
#     print({}[9])
# except IndexError:
#     print("здесь была бы ошибка с индексом")
# except TypeError: # lovim specificheskuu owibku
#     print("здесь была бы ошибка с типом данных") # poimal owibku i ne vydelyaetsya krasnym
# except NameError:
#     print("здесь ошибка с именем. Такой переменной нет")
# except ZeroDivisionError:
#     print("здесь нельзя делить на 0")
# except KeyError:
#     print("zdes slovar'")
# except LookupError:
#     print("ощибка поиска элемента")
#
#
# try:
#     print(1 + "2")
# except:
#     print("любаы ошибка под классом Exception") #vozmet vse vidy owibok


# import sys #sistemnyi modul, po etoi moduli mojno posmotret' lubye vidy owibok i opisanie
# randomList = ["q",0, 13] #elementy dlya proverki
# for entry in randomList: #berem kajdyi element i proveriaem
#     try:
#         print("The entry is", entry) #ukazyvaem s chem rabotaem
#         print(1/entry) #kakoi otvet deleniia
#     except: #esli delenie ne rabotaet to sms owibki snizu
#         print("Oops!", sys.exc_info()[0], "occured.") #execution in form, 0 dlya korotkogo soobweniia, chtoby pokazal nujnoe



# raise ZeroDivisionError - mojno zapisyvat' sobstvennye owibki i zapustit'



# try:
#     num = int(input("vvedite polojitelnoe chislo: "))
#     if num <= 0:
#         raise ValueError("Eto chislo otricatelnoe!")
# except ValueError:
#     print(ValueError)
#
# try:
#     num = int(input("vvedite polojitelnoe chislo: "))
#     if num <= 0:
#         raise ValueError("Eto chislo otricatelnoe!")
# except ValueError as ve:
#     print(ve)



# #else - pohoj na if-elif-else
# try:
#     print("kakoi-to code") #esli net owibki pokazhet chto vse normalno
# except:
#     print("esli owibka to ee poimali")
# else:
#     print("no esli owibki net, to vse normal'no")



#
# try:
#     print(x) #esli zdes vse pravilno to pokazalo by owibok net
# except:
#     print("kakaya-ta owibka")
# else:
#     print("net owibok")
# finally: #finally rabotaet nezavisimo ot try, except, else
#     print("Block zakonchen")





# my_list = ["hi", "hey", "hiya"]
# user = int(input("vvedite index: ")) # polzovatel' vvodit chislo
# try:
#     print(my_list[user]) # kotoryi ispolzuetsya dlya vyvoda elementa v spiske
# except IndexError: # obrabotka owibki, mojno napisat' Exception chtoby iskluchil vse owibki
#     print("owibka v indexe") # vydaem soobwenie



