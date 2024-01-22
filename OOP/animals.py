#multilevel inheritance

#Organism is like the Grandfather 
class Organism:
    
    alive = True

    def org(self):
        print("You're are an organism")

#Animal is the parent class
class Animal(Organism):

    def eat(self):
        print("This animal is eating")
    
    def sleep(self):
        print("This animal is sleeping")

#These are children classes
class Rabbit(Animal):
    def run(self):
        print("This rabbit is running")
class Fish(Animal):
    pass
class Hawk(Animal):
    pass

#objects
rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

print(fish.alive)
print(rabbit.eat())

rabbit.run()
print(fish.alive)
hawk.org()