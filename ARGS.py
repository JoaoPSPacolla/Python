#* args -> args is just a name. You can use whatever you want. The most important is the *  . All the arguments are goin to be transformed into a tuple (ordered and unchangable)

def add(*joao):
    sum = 0
    # joao[0] = 1 this is not allowed
    joao = list(joao) # this works because we tranformed the tupple into a list
    joao [0] = 10
    for i in joao:
        sum += i
    return sum
    
print(add(1,2))

def soma(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

print(soma(1,2,3,4,5,6))