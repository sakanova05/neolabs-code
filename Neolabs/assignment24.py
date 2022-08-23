class Penguin:
    species = "bird" #attribute classa - statisticheskii
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def hunt(self):
        print("hunt!")

    def swim(self):
        print("swimming cool")

lolo = Penguin ("lolo", "black&white")
print(penguin.name)
lolo.hunt()
lolo.swim()

