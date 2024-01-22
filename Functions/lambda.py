#functions written in 1 line and have the word lambda

# lambda parameters:expression --> It can have many parameters, but only one expression

'''def double(x):
    return x * 2'''
#This is how a normal function is created 

#Now, a lambda function
double = lambda x:x*2
multiply = lambda x,y:x*y
add = lambda x,y,z:x+y+z
print(double(2))
print(multiply(2,3))
print(add(1,6,9))

full_name = lambda first_name,last_name: f'Full name: {first_name} {last_name}' #Esse f é que nem o $ no JavaScript
print(full_name("João","Stradioto"))

age_check = lambda age:True if age >= 18 else False
print(age_check(19))

avaliacao = lambda nota:"Aprovado" if nota >=7 else ("Recuperação" if nota>=5  else "Reprovado")
print(avaliacao(5))