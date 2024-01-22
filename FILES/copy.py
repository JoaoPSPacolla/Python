#copyfile() = copies content of a file
#copy() = copyfile() + permisson mode + destinantion can be a directory
#copy2() = copy() + copie metadata

import shutil

shutil.copyfile('FILES/test.txt','C:\\Users\\joaop\\Music\\copy.txt') #THE orginal file , THE destination
shutil.copyfile('FILES/test.txt','copy.txt')