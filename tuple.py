#tuple = same to a list, but is unchangeable and ordered 

student = ("joao",19,"male") #in tuples don't use []. Use () instead

print(student.count(19))
print(student.index("male"))

for i in student:
    print(i)

if "Lucas" in student:
    print("Hello, Lucas!")
else:
    print("Hello, anyonelse")