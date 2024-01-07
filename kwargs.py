#**kwargs = It's like the *args,but intead of transform into a tuple. it creates a dictionary . And , it also need to have keyword arguments

def hello(**kwargs):
    #print("Hello "+kwargs['first']+ " " + kwargs['first'])
    print("Hello", end=" ")
    #for value in kwargs.values(): or
    for key,value in kwargs.items():
        print(value)
    
hello(title="Mr.", first="Bro",middle="Dude",last="Code")