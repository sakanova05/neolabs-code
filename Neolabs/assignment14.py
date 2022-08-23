student = {"name": "Madina",
           "age": "24",
           "job position": "Junior lawyer",
           "hobby": ["dancing", "watching movies", "makeup"],
           "favorite movie": "Pulp fiction",
           "favorite cuisine": ["Japanese", "European"],
           "favorite book": "The Subtle Art of Not Giving a Fuck"}
for key, value in student.items():
    if type(value) == list:
        print(*value, sep= ", ")
    else:
        print(value)