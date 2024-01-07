#dictionary = changeable, unordered, acess value quickly. Always use {}
#It's list that you acess the members by 'kind of' and ID, that they have

#Uma lista tem [] e você poderia fazer uma lista de capitais. Ex: capitais = ['Washington', 'Brasilia', 'Moscow']. Porém, você não consegue identificar esses valores. Portanto, através de uma lista, não é possível qual dizer, por exemplo, que Brasilia é a capital do Brasil, mas por um dicionário, sim

#Capitals - dictionary
#Countries - Keys
#The capitlas of the countries - values
capitals = {'USA': 'Washington DC', 
            'India': 'New Dehli',
            'Brasil': 'Brasilia',
            'Russia': 'Moscow'}

print(capitals['Russia']) 
print(capitals.get('Germany')) #When using GET, if the key you're searching doesn't exist, it won't happen an error
print(capitals.keys())
print(capitals.values())
print(capitals.items())

capitals.update({'Germany': 'Berlin'}) #add new one
capitals.update({"USA": 'Los Angeles'}) #changin one
capitals.pop('Russia')

print()

for key,value in capitals.items():
    print(key,value)

capitals.clear()
print(capitals.items())
