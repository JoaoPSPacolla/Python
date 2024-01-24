#Sort() method - used with lists --> Organizes ascendenting or descententing with if use a reverse=True . If the arguments are strings, it organizes alphabeticly 

#This is a list of tuples
students = [("Squidward", "F", 60),
            ("Sandy", "A", 33),
            ("Patrick","D", 36),
            ("Spongebob","B", 20),
            ("Mr.Krabs","C", 78)]

students.sort(reverse=True)
for i in students:
    print(i)

print()

age = lambda n:n[2]
students.sort(key=age)
#ages = sorted(students,key=age)
for i in students:
    print(i)

print()

grade = lambda i:i[1] #for each grades, take the column 1 (remember, it's starting counting by zero)
students.sort(key=grade)  # sorts current list
sorted_students = sorted(students,key=grade) # sorts and creates a new list

for i in sorted_students:
    print(i)

print()


animals = ["Dog","Cat","Fish"]
#animals = ("Dog","Cat","Fish") The sort won't work on this because it's a tuple REMEMBER [] List () Tuple . A tuple is ordered and unchangeable, so it makes sense that you can't use a .sort()

animals.sort(reverse=True)

for i in animals:
    print(i)

print()

#But you can use a tuple and others iterable with a SORTED function 

animal = ("Dog","Cat","Fish")
sorted_animal = sorted(animal, reverse=True) #take out the reverse true and will be alphabeticly organized 

for i in sorted_animal:
    print(i)