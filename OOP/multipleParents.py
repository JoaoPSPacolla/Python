#multiple inheritance (parents) --> When a child class derivatives from more than just one parent class

class Prey:
    prey = True

class Predator:
    predator = True

class Rabbit(Prey):
    pass
class Hawk(Predator):
    pass
class Fish(Prey,Predator): #This is a multiple inheritance
    pass

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

print(fish.predator)
print(fish.prey)