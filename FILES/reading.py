
try:
    with open('readingFile.txt') as file:
        print(file.read())
except FileNotFoundError:
    print("File not found : ( ")


#print(file.closed)