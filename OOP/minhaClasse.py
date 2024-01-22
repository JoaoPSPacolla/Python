from car import Car

car1 = Car("Ferrari","red","ROMA",2024)

print(car1)

Car.wheels = 3
print(car1.wheels)

car1.drive()
car1.stop()

car1.wheels = 2
print(car1.wheels)

#you can acess clas variables without having an object

