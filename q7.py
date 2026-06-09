#q7
#task 1
class Car:
 def __init__(self,make,model,year):
  self.make=make
  self.model=model
  self.year=year
 def describe_car(self):
  print(self.year, self.make, self.model)
#task 2
obj_car=Car("Toyota","Corolla", "2020")
obj_car.describe_car()