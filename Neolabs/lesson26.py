# class MightiestWeapon:
#     name = "default name" # statistical attribute - attribute classa, nikogda ne menyaetsya, otnositsya ko vsem ob'ektam
#     def __init__(self, name): # dynamic attribute - attribute of object, naprotiv k konkretnym ob'ektam
#         self.name = name
#
# weapon = MightiestWeapon("sword")
# print(MightiestWeapon.name) # pokazhet imya klassa
# print(weapon.name) # pokazhet imya ob'ekta

# self - kluchevo slovo kototroe pomagaet to refer samoi sebe

class Bird: # roditel'skii class
    def __init__(self):
        print("Bird is ready")

    def whoIsThis(self): # metod
        print("Bird")

    def swim(self):
        print("Swim faster")

# class Penguin(Bird): # roditel'skii class
#     def __init__(self):
#         super().__init__() # super() pozvolyaet vospol'zovatsya metodom rod. klassa
#         print("Penguin is ready")
#
#     def whoIsThis(self): # perezapis - overridng
#         print("Penguin")
#
#     def run(self):
#         print("run faster")
#
# peggy = Penguin() # ob'ekt i pokazhet Bird and Penguin is ready potomu chto super.init ispolzovali
# peggy.whoIsThis()
# peggy.swim()
# peggy.run() # snachala nahodit penguin, potom whoisthis potom deistvie


# class Person:
#     def walk(self):
#         print("chelovek hodit")
#
#     def cry(self):
#         print("chelovek plachet")
#
# class Child(Person):
#     def crawl(self):
#         print("rebenok polzaet")
#         super().walk() # super funkciia - nujna konkretnye metody vyzvat' pri zapuske i neskolko metodov, dlya vyzova metoda ot roditelya

# kid = Child()
# kid.crawl()
# kid.cry()
#
# class F14(Jets):
#     def __init__(self):
#         self.name = "F14"
#         self.origin = "USA"
#
# a = F14
# print(a.origin)
# print(a.name)


# class Jets:
#     model = None
#     country = 0
#     name = "kakoi-to samolet" # otnositsya ko vsem samoletam
#     def __init__(self, name, country):
#         self.name = name # otnositsya k odnomu samoletu
#         self.origin = country # pereprisvoili country k origin
#
# first_item = Jets("F16", "USA")
#
# a = first_item.name
# b = first_item.origin #atributte ob'ekta
# print(a)
# print(b)class Jets:
# #     model = None
# #     country = 0
# #
# #
# #     def __init__(self, name, country, quantity):
# #         self.name = name # otnositsya k odnomu samoletu
# #         self.origin = country
# #         self.quantity = quantity
# #
# # first_item = Jets("f14", "USA", 123)
# # second_item = Jets("Mirage2000", "USA", 345)
# #
# # total = first_item.quantity + second_item.quantity
# # print(total)


#
# class Nobel:
# def __init__(self, category, )

class Feline: # sozdali roditel'skii class i dobavili dva metoda
    def play(self):
        print("cat is playing")

    def scratch(self):
        print("cat is scratching the floor")

class HouseCat(Feline):
    def play(self):# perezapis' or overriding, pomenyali metod
        print("domashnie koshki ne igrautsya")

    def voice(self):
        print("Mewo!") # rasshirenei - extending, novyi metod dobavili


cat1 = HouseCat()
cat1.play()


