class Motorcycle:

    color = None

def change_color(motorcycle, color):

    #You can pass an object as paremeter with no problem, since the methods/attributes exists in the class of the  object you passed

    motorcycle.color = color

motorcycle1 = Motorcycle()
motorcycle2 = Motorcycle()
motorcycle3 = Motorcycle()

#Passing an object as peremeter 
change_color(motorcycle1,"blue")
change_color(motorcycle2,"red")
change_color(motorcycle3,"green")

print(motorcycle1.color)
print(motorcycle2.color)
print(motorcycle3.color)