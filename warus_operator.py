
#if you try to do this bellow, it will occur an error
#print(happy = True)

#for this, you can use an warus operator :=
print(happy := True)

print("Write quit to finish the program")

foods = list()

'''while True:
    food = input("What food do you like? ")
    if food == "quit":
        break
    foods.append(food)'''

#This same code can be written like this:

while food := input("What food do you like?: ") != "quit":
    foods.append(food)

print(foods)