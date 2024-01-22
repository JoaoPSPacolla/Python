class Animal():
    #When use multiple chining, it's necessary to put a return object after each method
    def eat(self):
        print("This animal is eating")
        return self
    def run(self):
        print("This animal is running")
        return self
    def sleep(self):
        print("This animal is sleeping")
        return self


rabbit = Animal()
#Using multiple methods at the same time
rabbit.eat().run().sleep()