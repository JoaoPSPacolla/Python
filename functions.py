def hello(name):
    print("hello! "+name)

#oi = ''
while True:
#while (oi.lower() != 'n�o'):
    oi = input("Digite se nome: ")
    
    if(oi.lower() == 'n�o'):
        break;
    else:
        hello(oi)
        
        