#Nested functions - functions inside functions
'''
num = input("Enter a whole positive number: ")
num = float(num)
num = abs(num)
num = round(num)
print(num)

To don't use too many lines like this example above, nasted funtions provide a more simplistic way 
'''
num = round(abs(float(input("Enter a whole positive number: "))))
print(num)

print(round(abs(float(input("Enter a whole positive number: ")))))