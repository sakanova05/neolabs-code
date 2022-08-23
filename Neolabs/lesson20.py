#
# def data(name, age, occupation, *hobbies): #3 obyazatelnyh parametra i 1 opcional'nyi
#     print("Имя:", name)
#     print("Возраст", age)
#     print("профессия:", occupation)
#     print("Хобби:", hobbies)
# data("Farrad", 123, "student", "swimming", "surfing", "playing")
#
# def my_fun(hobby, name, age): #imennovannye argumenty
#     print(name, age, hobby)
# my_fun("swimming", name = "Alex", age = 123)

# print("hello, my name is {}. My balance is {}".format("Alex", 123))
# print("hello, my name is {0}. My balance is {1}.format("Alex", 123))
#
# y = 10
# def output():
#     y = 20 #local'naya peremennaia s drugim znacheniem
#     print(y)# peremennaia imeet prioritet pri vyvode
# output() #pokazhet to, chto vnutri funkcii - 20
# print(y) #pokazhet global'nuiu peremennuiu - 10

# y = 1000
# def my_fun1():
#    global y #cherez kluchevoe slovo mozhno meniat' znacheniya
#     y = y +1 # bez kluchevogo slova, peremennaia ne rabotaet
#     print(y)
# print(y)
# my_fun1()

# x = 10
# def num():
#     print(x) #esli peremennaia snaruzhi, ee mozhno ispol'zovat' a esli peremennaia sozdana vnutri, ee nel'zya snaruji ispol'zovat'
# num()
#
# def num1():
#     y = 10
#     print(y)

def greet(name):
    """
    Privetstvuiu cheloveka, ch'e imya peredano v parametrah

    """
    print("Hello " + name + ". Good morning!")
greet("Alex")

# def output():

