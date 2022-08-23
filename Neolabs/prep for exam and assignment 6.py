# Prep for exam 2 - 3rd week of studies
# example with operator if
# age = int(input("введите возраст: "))
# if age < 0 or age > 150:
#     print("invalid")# always first validity of code then go further to the positive
# elif age < 18:
#     print("nelzya")
# elif age >= 18:
#     print("mozhno")
# elif age < 0 or age > 150:
    # print("invalid")


# assignment 4
# else:
# always print is below

# total = int(input("vvedite obwee kolichestvo urokov: "))
# attended = int(input("vvedite kolichestvo posewennyx zaniatii: "))
# result = attended/total * 100
# if result >= 75:
#     # print(result, "mozhno") #you may also add int before reult if want to rround number
# else:
#     print(result, "nelzya")

# primer s while s 1 d0 20
# candy = 1
# while candy <= 20: #blok vnutri while rabotaet esli uslovie vypolneno
#     print(candy)
#     candy = candy + 1
# you can either write as count += 1
#
# candy = 10 # s 10 do 1
# while candy > 0:
#     print(candy)
#     candy = candy - 1

# count = 0 # peremennia dlya scheta s 1 do 10
# total = 0 # peremennaia dlya hraneniya summy
# while count < 10: # tol'ko uslovie ne mojem skladyvat' s while
#     count += 1
#     total = total + count # either you can total += count tut my schitaem summu
#     # prohodim wag
#     print("счет", count, "сумма", total)

#
# count = 0
# total = 0
# while count < 1000:
#     count += 1
#     total += count
#     print(count, total)


# primer s pokupatelyami
count = 0
# while count < 5:
#     user = int(input("введите возраст: "))
#     if user >= 18:
#         print("mozhno")
#     else:
#         print("nelzya")
#     count += 1

# ages = [12,13,18,24,44]
# # print(ages[0]) => primer odnogo vyvoda
# count = 0
# while count < len(ages):
#     print(ages[count])
#     count += 1

# ages = [12,13,18,24,44]
# count = 0
# while count < len(ages): # 0 < 5
#     if ages[count] >= 18: # na kazhdoe novoe chislo na indexe sravnivaetsya s 18
#         print(ages[count], "можно") #vyvodim chislo
#     else:
#         print(ages[count], "нельзя")
#     count += 1 # perehodim k sled wagu

count = [1,2,3]
print(len(count))

#proverka chisel na otchetnost'
count = 0
while count < 20:
    if count % 2 == 0: #esli delitsya na 2 s ostatkom 0
        print(count, "четное")
    else:
        print( count, "нечетное")
    count += 1
