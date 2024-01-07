#index operator []

name = 'joao Paulo'

if (name[0].islower()):
    name = name.capitalize()
    
#substrings
first_name = name[:4].upper()
last_name = name[5:].upper()
last_charcater = name[-1]
    
print(name)
print(name.lower())
print(first_name)
print(last_name)
print(last_charcater)