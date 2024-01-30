#filter (function, iterable)
#Filter só pxa resultados que forem TRUE

friends = [("Rachel",11),
           ("Monica",20),
           ("Joel",19),
           ("Chandler",18),
           ("Phoobe",21),
           ("Ross",24)]

age = lambda data: data[1] >= 18 

drink = filter(age,friends)

print("People allowed to drink:")
for a in drink:
    print(a)