food = ['pizza','hotdog','soda','chicken']

print(food)
'''print(food[0])
food[1] = "lemon"
print(food[1])
print(food[2])
print(food[3])
#print(food[4]) out of range error'''

for f in food:
    print(f)

print()
food[1] = "lemon"
print(food[1])

#Functions

food.pop() #remove the last one
food.append("ice cream") #add in the end
food.insert(0,"cake") 
food.remove("soda")
food.sort() #organize alphabetcally
# food.clear() remove everything

print(food)
