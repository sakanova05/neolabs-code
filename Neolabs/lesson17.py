# def greet(name, age, hobby): #parametry
#     """Функция приветствует""" #documentaciia
#     print(f"Добро пожаловать! {name}, {age}, {hobby}")
# greet("Alex", 123, "swimming") # arguments
# print(greet.__doc__) #stroka documentacii, daet ob'yasnenie i napominaet chto za kod
#
# def info():
#     return "hello" #vozvrawaet znachenie computeru no ne pokazyvaet, chtovby pokazyval nujno napisat' pribt
# print(info())


#
# def my_fun():
#     return "hi" #vozvrawenie znacheniia i vyhod iz funkcii
#     print("hi")
#     print("hiya")
#     print("privet")
# my_fun()

#
# x = 10 #peroe znachenie x
# def num():
#     print(x)
# x = 123 #pereopredelili x na 123
# num() # vyvodit posledne, chto zapomnil

# my_list = []
# my_list.append(1) # primer vstroennoi funkcii


# def adder(x,y,z):
#     print(x+y+z)
# adder(123, 145, 567) # slojili tri potomu chto tri chisla ukazano v opredelenii


# def adder(*numbers): # funkciia dlya skladyvaniia chisel
#     total = 0
#     for num in numbers: # prohodimsya po chislam
#         total += num # poschitaem summu
#     print(total)
# adder(24,56,7,8)
# adder(67,89,90)


# my_tuple = (1,2,3,45) # primer raboty s kartejom
# for element in my_tuple:
#     print(element)
#
# def output(*data): # args - peredaet v argumenty kortej
#     print(type(data))
# output()

# pervyi sposob vyvoda
# student = {"name": "Alex",
#            "age":123,
#            0:"hey"}
# print(student["name"]) #dlya vyvoda iz slovarya nujen kluch
# for key in student: #prohodimsya po klucham
#     print(key, student[key]) # vyvodim kluch i ego znachenie
#
#
# # vtoroi sposob vyvoda
# for key, value in student.items():
#     print(key, value)



# # funkciia kwargs
# def intro(**data): #kwargs - peredaet slovar' kak argument
#     for key, value in data.items():
#         print(key, value)
# intro(name = "alex", age = 123, hobby = "swimming")


# def names(*data):
#     for name in data:
#         print(name)
# names("Alex", "Marina")


# def num():
#     x = 10 # snachala bylo 10
#     print(x)
# x = 123 #pereimenovali na 123
# num() # vyzvali funkcii i znacheni stalo 10, vnutri imeet prioritet






