#LIST COMPREHENSIONS ARE A WAY TO CREATE LISTS SHORTLY

#This is how we can calcualte the square of 11 numbers without list comprehension

squares = [] #an empty list
for i in range(1,11): #a for 
    squares.append(i*i) #finding the square of each element and adding to the list
print(squares) 

#Now, with list comprehension
square = [i*i for i in range(1,11)]
print(square)

#list = [expression - for]

#***************************************************************************************************

students_grade = [100,90,80,70,60,50,40,30,0]

passed_students = list(filter(lambda x:x>=60,students_grade)) #Basicamente, o filter faz: em students_grade quem tem uma nota maior ou igual a 60. E tudo isso é transformado em uma lista
print(passed_students)

#a bigger list comprehension
passed_student = [i for i in students_grade if i >= 60] #you can't put else here. If you wanna use
print(passed_student)
 
#list = [expression - for - if] :or you can do this, if you need an else statement :  list = [expression - if/else - for ] 

passeds_students = [i if i >= 60 else "FALSE" for i in students_grade ]
print(passeds_students)

