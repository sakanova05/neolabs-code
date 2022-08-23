for i in range(-10, -1):
    print(i)

def clock(hour, minute):
    print("время: ", hour, minute)
clock(14, 22)


class Dog:
    def walk(self):
        print("*walking*")
        def speak(self):
            print("Woof!")

class JackRussellTerrier(Dog):
    def speak(self):
        print("Arff!")

bobo = JackRussellTerrier()
bobo.walk()


# class Wolf:
#     def __init__(self, color, age):
#         self.color = color
#         self.age = age
#
# wolves = Wolf()
# wolves.hunt()
# wolves.run()


# my_list = [element for element in range(5)]
# print(my_list)


list1 = [element for element in range (1, 21)]
print(list1)
