# # chislovoi tip
#
# num = "123"
# print(len(num))
#
# num = 123
# num = str(num) # pereprsivoili znachenie
# num = int(num) # type - comanda dlya vyvoda
# print(type(num))
#
# x=5
# y=123
# print(int(5.13))
# text = "321"
# text = int(text) # prisvoili chislo
#
# num1 = 3.9
# num1 = int(num1)
# print(type(num1)) # sokrawaet do celogo chisla
#
# print(bool(123)) # krome 0 or empty are true
# print (bool("hey")) # krome empty are true
#
# text1 = "              "#probel toje schitaetsya za chast' stroki
# text1 ="!@$$$      "
# print(len(text1))
# print (text1[18]) #

# posledovatel'nyi tip'

lessons = ["math", "physics", "english"]
print(lessons[0])
print(len(lessons))
#          0          1       2
colors = ["orange", "pink", "black"]
print(colors[2])     # tip posledovatel'nosti - list
print(len(lessons))
print(type(lessons))

my_tuple = ("1",)
print(my_tuple)

# my_tuple1 = ()
# my_tuple2 = ()
# print(id(my_tuple1))   # ne menyaet ID v otlichii ot list
# print(id(my_tuple2))

my_list1 = ()
my_list2 = ()
print(id(my_list1))
print(id(my_list2))

my_list = ["study", "twerk", "eat"]
# print(len()) pokazyvaet dlinu spiska
print (my_list)
del my_list[1] # del tolko index
print (my_list)

my_list.append("watch tv") # dobavlyaet tol'ko odin element
print(my_list)
# my_list.insert(1, "watch TV") chtoby postavit' na kakuyu-to poziciu
print(my_list)

# comanda pop
my_list.pop(0) #udalyaet  i soxraniet ostal'nye chasti a del net
print(my_list[1])
