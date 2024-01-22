'''duck typing = concept where the class of an object is less important than the methods/attributes
class type is not checked if minimum methods/attributes are present
“If it walks like a duck, and it quacks like a duck, then it must be a duck.” '''

class Duck:

    def walk(self):
        print("This duck is walking")

    def talk(self):
        print("This duck is qwuacking")

class Chicken:

    def walk(self):
        print("This chicken is walking")

    def talk(self):
        print("This chicken is clucking")
        
    #This can be here (or in the duck class) as long as they not been called in the duck tipping method
    '''def swim(self):
        print("This duck is swimming")'''

class Person():

    def catch(self, duck): #see that here is refering a duck object
        duck.walk()
        duck.talk()
        #duck.swim() If you summon up a method that doesn't exist in one of the classes , them the duck tipping no loger will work
        print("You caught the critter!")


duck = Duck()
chicken = Chicken()
person = Person()

person.catch(duck) #but here it's been passed a chicken and that's works. This happens because chicken and duck has the same paremeters 