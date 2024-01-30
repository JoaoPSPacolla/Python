#reduce (function, iterable) --> it transforms a bunch of elements in just one

import functools
letter = ["H","E","L","L","O"]
word = functools.reduce(lambda l1,l2: l1+l2,letter) #concatena as duas primeiras letras e vai pegando as próximas enquanto houver
print(word)

numbers = [5,4,3,2,1]
factorial = functools.reduce(lambda n1,n2: n1*n2,numbers)
print(factorial)
