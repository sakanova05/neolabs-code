# assignment9, sposob 1

# nums = input().split()
# num1 = int(nums[0])# oboznachili 1 element kak celochislennyi tip
# num2 = int(nums[1]) #toje samoe so vtorym
# if num1 != num2:# esli ne ravno
#     print(num1 + num2) #togda skladyvaem
# else:
#     print((num1 + num2)*2) #esli ravny, togda skladyvaem

# sposob2
# nums = input().split() # spisok strok
# nums = list(map(int, nums)) # prevratim stroki v chisla
# num1 = nums[0] # vzyali pervoe chislo
# num2 = nums[1] # vzyali vtoroe chislo
# if num1 != num2:
#     print(num1 + num2)
# else:
#     print((num1 + num2)*2)
#
# sposob3
# nums = input().split() # poluchili spisok stroku chisel
# nums = list(map(int, nums)) #prevratili v spisok celochislennyh
# print(round(sum(nums)/len(nums)) #vyveli summu
#
#
# array - массив
# list - список

# countries = ["Russia", "China", "USA"]
# del countries[0]
# print(countries)
# countries.append("Japan")
# print(countries)
# for i in countries: # poschitali cskolko bukv v kazhdom elemente
#     print(i, len(i))

# to je samoe bez len a s count
# countries = ["Russia", "China", "USA"]
# del countries[0]
# print(countries)
# countries.append("Japan")
# print(countries)
# for country in countries: #vlozhennye cikly
#     count = 0 # obnovliaem schetchik, dlya kazhdoi strany schitaem letters, esli count budet do for to poschitaet vse bukvy a ne kazhdogo slova
#     for letter in country: #cikl vnutri cikla
#         count += 1 #schitaem bukvy
#     print(country, count)

# lesson 11
# Difference of the same method but in different circumstances

# name = "Farrad"
# name = list(name) #peopredeliaem peremennuiu
# print(name)
#
# name1 = "Farrad"
# print(list(name1)) #pokazyvaet v vide spiska
# print(name1) #pokazyvaet staruiu peremennuiu stroku


# my_set = {9,6,7,3,4,2,1}
# print(sorted(my_set)) #mozhno ispolzovat dlya raznyh tipov dannyx a takje izmenyaet, sama peremennia set ne meniaetsya
# print(my_set) #sety ne uporyadocheny
#
#
# mylist = [54,78,90, 87]
# mylist.sort(reverse=True) #sortirovka ot bolshego k menwemu
# print(mylist)

# pervyi sposob copy
# list2= [1,2,3] # old list
# newlist = list2.copy() # new list - copied list
# list2.append(4) # while changing the old list the new list does not change
# print("Old list", list2)
# print("New list", newlist)

# vtoroi sposob copy
# old_list = [4,5,6] # old list
# new_list = old_list # new peremennaia ukazyvauwaia na old list
# old_list.append(7) # while changing, the both will change cuz it refers to the first peremennaia
# print(old_list)
# print(new_list)


# two dimensional list

# two_dlist = [[1,2,3],
#             [4,5,6],
#             [7,8,9]]
# print(*two_dlist, sep = "\n")# odin iz sposobov dlya vyvoda v stolbik


# two_dlist = [[1,2,3],
#             [4,5,6],
#             [7,8,9]]
# for one_dlist in two_dlist: #rabotaem so spiskami
#     for element in one_dlist: # rabotaem s chislami
#         print(element, end = " ") #vyvodim sviazannye chisla riadom
#     print() # otdeliaem otdelnye spiski novoi strokoi


# two_list = [[1,2,3],
#             [4,5,6],
#             [7,8,9]]
# one_list = two_list[0] #vytawili odnomernyi spisok ot 1 do 3
# print(one_list[0]) # vytawili element iz pervogo spiska



# two_list = [[1,2,3],
#             [4,5,6],
#             [7,8,9]]
# for i in range(len(two_list)): # dlya i ot 0 do 2
#     for k in range(len(two_list[i])): # dlya k ot 0 do 2
#         print(two_list[i][k], end = " ")
#     print()

# # sposob s pomow'u while
# two_list = [[1, 2, 3],
#             [4, 5, 6],
#             [7, 8, 9]]
# count = 0 # schetchik dlya naruzhnogo cikla
# while count < len(two_list): # poka 0 menwe dliny spiska
#     count2 = 0 # chtoby brat' s indexa 0, schetchik dlya chisel vnutri spiska
#     while count2 < len(two_list[count]): # poka 0 menwe chem dlina vnutrennego spiska
#         print(two_list[count][count2], end = " ") #vyvodim otdelnye elementy
#         count2 += 1
#     count += 1
#     print()



# two_list = [[1, 2, 3],
#             [4, 5, 6],
#             [7, 8, 9]]
# for record in two_list:
#     print(*record) #raspokovyvaem, ubiraem kvadratnye skobki, vytaskivaet elementy po otdelnosti i pokazyvaet


my_list = [["hey", "hi", "hiya"],
          ["priv", "privet", "zdravstvuite"]]
print(my_list[1][2])
print(my_list[1][1][3])
