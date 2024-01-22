import os
import shutil

path = 'FILES/empty'

try:
    #os.remove(path) #remove arquivos
    os.rmdir(path) #remove pastas
    #shutil.rmtree(path) this delete a directory that is not empty .TAKE care with
except FileNotFoundError:
    print("This file wasn't found")
except PermissionError:
    print("You're not allowed to do that")
except OSError:
    print("This directory is not empty")
else:
    print(path+" deleted")