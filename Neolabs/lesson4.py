# text = 'he said: "he\'s dying"' example of ignoring kovychki
# text1 = ''' he said: he's dying'''  also ignores kovychki
# animal =["cat", "dog", "parrot"]
# animal.append("hamster")
# del animal[1]
# animal.remove('cat')
# print(animal)
# cuisine = ["plov", "macaroons", "sushi"]
# cuisine.append("steak")
# print(cuisine)
# del cuisine[2]
# print(cuisine)
# cuisine.remove('macaroons')
# print(cuisine)

age = int(input("введите ваш возраст: "))
if age < 18:
    print("nelzya")
if age >= 18:
    print("mozhno")
elif age < 0:
    print("invalid")
elif age < 150:
    print("invalid")

user = int(input("введите ваш возраст: "))
if user > 150 or <= 0:
    print("invalid input")
elif user >= 18:
    print("mozhno")
elif user < 18:
    print("nelzya")