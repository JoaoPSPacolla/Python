#string
name = "joao" 
sobrenome = "pacolla"
nome_completo = name + ' ' + sobrenome 
print("My name is "+ nome_completo)
print(type(nome_completo))

#int
age = 19 
age += 1
print(age)
print(type(age))

# to concat variables, it's necessary that both has the same type
'''erro = name + age
print(erro)'''

#But, you can convert the one of the variables to have the same type of the other 
certo = (name + " " + str(age))
print(certo)

#float
height = 1.78
print("My height is: " + str(height))
print(type(height))

#boolean
human = True
print("Are you a human? " + str(human))
print(type(human))
