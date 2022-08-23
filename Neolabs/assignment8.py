st = input("insert text: ").lower()
subst = input("what did you look for? ").lower()
if subst in st:
    print("Contact!")
else:
    print("nope!")