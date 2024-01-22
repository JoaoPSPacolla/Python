import os

source = "FILES/movingFolder" # you can move files or folders
destination = "C:\\Users\\joaop\\Music\\folder.txt"

try:
    if os.path.exists(destination):
        print("This file is already there")
    else:
        os.replace(source,destination)
        print(source+" was moved")
except FileNotFoundError:
    print(source+" was not found")