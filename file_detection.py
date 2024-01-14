import os
import time

path = "C:\\Users\\joaop\\Desktop\\Jogos Zerado.xlsx"



if os.path.exists(path):
    print("This location exist")
    if os.path.isfile(path):
        print("This is a file")
    elif os.path.isdir(path): #is directory - pasta
        print("This is a directory")
    time.sleep(2)
    os.system("cls")
else:
    print("This location doesn't exist")
    time.sleep(2)
    os.system("cls")