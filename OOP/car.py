class Car:  

    wheels = 4 #This is a class variable . It's out of the constructor

    #Constructor -> init
    def __init__(self,make,color,model,year):       
        self.make = make 
        self.color = color
        self.model = model  
        self.year = year
        #self é que nem o this

    def drive(self):
        print("This "+self.model+" car is moving")

    def stop(self):
        print("This "+self.make+" car's stopped")

