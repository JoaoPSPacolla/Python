class Animal():

    def eat(self):
        print("This animal is eating")

#Overwrite - overwrite a parent function 
class Rabbit(Animal):
    def eat(self):
        print("This rabbit is eating a carrot")

rabbit = Rabbit()
rabbit.eat()
