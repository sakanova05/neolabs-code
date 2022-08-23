my_book = {"title": "War and peace",
           "author": "Lev Tolstoy",
           "year": 1867,
           "genre": ["novel", "historical fiction"],
           "ISBN": 9785699353019,
           "awards": None}
# print(my_book)

# my_book["co-author"] = "Alex Farrad"
# my_book["awards"] = "best seller"
# print(my_book["genre"]) #shows element with key, if there is no key then it will show error
# print(my_book.get("name"))
# del my_book["year"] # if there is no element, then will show None
# print(my_book.get("year"))

# favourite_band = {"title": "BTS",
#                   "genre": "K-pop"}
# favourite_band["participant"] = "Mike"
# print(favourite_band)
# favourite_band["title"] = "Viagra"
# print(favourite_band)
# del favourite_band["participant"]
# print(favourite_band)
# var = favourite_band.pop("genre") # udalili kluch i sohranili znachenie
# print(favourite_band)
# var1 = favourite_band.popitem()
# print(favourite_band)

# subject = {"title": "math",
#            "teacher": "Farrad"}
# quantity = int(input("vvedite  kol-vo komand: "))
# for element in range (quantity):
#     x = input("vvedite komandu: ")
#     if x == "add": #esli komanda dlya dobavleniia, to zaprosim kluch i znachenie
#         key = input("vvedite kluch: ")
#         value = input("vvedite znachenie: ")
#         subject[key] = value #dobavim kluch i znachenie v slovar'
#     print(subject)
# elif x == "del":
#     key = input("kakoi kluch udalit? ")
#     del subject[key]
# else:
#     print("takoi komandy net") #esli komanda ne ta, to takoi vyvod


# zadacha s bukvami
# my_str = input("vvedite 1 stroku: ").lower()
# my_str2 = input("vvedite vtoruiu stroku: ").lower()
# if my_str == my_str2:
#     print("equal")
# elif my_str < my_str2:
#     print(-1)
# else:
#     print(1)

user = input("vvedite stroku: ")
new_str = " "
for element in user:#dlya bukvy v slove
    if element not in "auoie": #esli bukva neglasnaiia
        new_str += "." #stavim tochku vperedi
        new_str += element #potom postavim soglasnuiu bukvu
print(new_str)