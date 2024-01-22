def hello(name):
    print("hello! "+name)

#oi = ''
while True:
#while (oi.lower() != 'não'):
    oi = input("Digite se nome: ")
    
    if(oi.lower() == 'não'):
        break;
    else:
        hello(oi)
        
        