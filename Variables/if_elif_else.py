
while True:
    age = int(input("How old are you? "))

    if age < 0:
        break

    if not(age >= 18):
        print("No")
'''
    if age >= 18:
        print("You are allowed to drink")
    elif age >= 15 and age < 18:
        print("You can taste, but only a cup")
    elif age < 3 or age > 200:
        print("You are a baby or propably dead")
    
    else:
        print("You can't even enter")'''

        