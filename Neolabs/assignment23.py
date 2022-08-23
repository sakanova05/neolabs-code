class Dog:
    def __init__(self, name, age): # atributy - svoistva
        self.name = name
        self.age = age

    def bark(self):
        print("bark, bark!")
bobi = Dog("Bobi", 7)
print(bobi.name)
bobi.bark()
bobi.chase()