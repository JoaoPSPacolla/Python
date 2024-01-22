
text = "Good Bye"  #If you chabge this and the file was already created, then, it will be overwritten

with open('FILES/test.txt','a') as file:  #Como padrão vem o r de read, mas você pode alterar para w, por exemplo, que é para write. a is APPEND
    file.write(text)