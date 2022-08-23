# film = {"title": "Pulp fiction",
#         "genre": ["comedy", "drama"],
#         "year": 1994,
#         "budget": 8.5000000,
#         "actors": ["John Travolta", "Uma Thurman", "Samuel L. Jackson"]}
# print(film)
# #
# var = film.pop("budget")
# var1 = film.popitem()
# print(film)
# print(var)
# print(var1)
#
# cast = film['actors']
# cast.remove("John Travolta")
# print(film[])


# {"city": "Bishkek",
#  "Datetime": "08/06/2022 - 19:44",
#  "temprature": 24}
# print()
#
# film = {"title": "Pulp fiction",
#         "genre": ["comedy", "drama"],# dva i bol'we spiski to est skobki kvadratnye
#         "year": 1994,
#         "budget": 8.5000000,
#         "actors": ["John Travolta", "Uma Thurman", "Samuel L. Jackson"]}
# for key, value in film.items(): #dlya klucha-znacheniia vnutri slovaria
#     print(key, value) #vyvesti kluch-znachenie
# film.clear()
# print(film)

#
# grades = {"math": 88,
#           "Eng":55,
#           "python":99}
# print(grades["Eng"]) #1 sposob
# print(min(grades.values())) # 2 sposob


#vyvodim skol'ko spiskov
film = {"title": "Pulp fiction",
        "genre": ["comedy", "drama"],# dva i bol'we spiski to est skobki kvadratnye
        "year": 1994,
        "budget": 8.5000000,
        "actors": ["John Travolta", "Uma Thurman", "Samuel L. Jackson"]}
count = 0
for key, value in film.items(): #dlya klucha-znacheniia
    if type(value) == list: #esli tip znacheniia raven spisku
            print(value) #vyvodim ego
            count += 1 # dobaliaem k schetchiku + 1
print(count)

# chtob vyvesti bez skobok i kavychek
for key, value in film.items(): #dlya klucha-znacheniia
    if type(value) == list: #esli tip znacheniia raven spisku
            print(*value, sep= ", ") #vyvodim ego
    else:
        print(value)
