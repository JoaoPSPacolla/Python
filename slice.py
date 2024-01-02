name = "Joao Paulo"

#first_name = name [0:4]
first_name = name [:4]
print(first_name)

letter = name[1]
print(letter)

#two = name[0:11:2] 
two = name[0::2] 
print(two)

reversed_name = name[::-1]
print(reversed_name)

#SLICE

website = "http://google.com"
slice = slice(7,-4) #começa na sétima letra e para na quarta da  direita para esquerda
print(website[slice])