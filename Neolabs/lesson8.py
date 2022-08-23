# capital = input("insert capital: ")
# capital. capitalize()
# print(capital)

# text = "Let it be, let it be, let it be"
# result = text.find("let it be") # register of letters has a meaning, register means capital or not the letter
# print(result)

# sentence = "python is fun"
# result = sentence.index("is fun")# shows the index of the sentence
# print(result)




# students = ["Meka", "Steve", "Leila", "Aika"]
# grades = [99, 78, 65, 100]
# max_grade = max(grades) #maximum grade
# index_max = grades.index(max_grade) # maximum index - poziciu
# print(students[index_max]) #using index to find the name

# print("Hey {}, your balance is {}.".format("Madina", 500))
# print("Hey {0}, your balance is {1}.".format("Madina", 500))
# print("Hey {name}, your balance is {balance}.".format(name = "Madina", balance = 500))
# print("Hey {0}, your balance is {balance}.".format("Madina", balance = 500))
# name, balance = "Madina", 200
# print(f"Hey {name}, your balance is {balance}")

# nums = input("insert number: ")
# num1 = int(nums[0])
# num2 = int(nums[2]) # tol'ko dvuzhanchye pokazyvaet cifry
# print(num1 + num2)

# nums = input("insert number: ")
# nums = nums.split()
# num1 = int(nums[0])
# num2 = int(nums[1])
# print(num1 + num2)

# numbers = input().split() #spisok strok
# total = 0 # peremennaia dlia hranenia summy
# for num in numbers: # prohodimsia po strokam
#     total += int(num) # prevrawaem stroku v chislo i dobavliaem v summu
# print(total) # vyvod summy


# print([["delo" for elem in range(5) for element in range(5)]]) #example of list comprehension

text = "python is awesome, isn't it?"
sub_text = "is"
count = text.count(sub_text)
print(count)