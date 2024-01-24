#map (function, iterable) #iterable can be objects, lists, tuples, sets, dictionaries, strings
# map aplica uma função para cada elemento do seu iterable 

store = [("shirt",30.00),
         ("pants",70.00),
         ("socks",20.00),
         ("jacket",200.00)]

to_euros = lambda data: (data[0],data[1]*0.19) #tranforming the R$ prices into EURO prices
'''def to_euros(data):
    return data[0],data[1]*0.19'''

store_euros = map(to_euros,store)

for i in store_euros:
    print([i])

num = 234.566767567567
print(round(num,4))