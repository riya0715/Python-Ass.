class Car:
    
    def __init__(self,name,mileage):
        self.name=name
        self.mileage=mileage
        
    def description(self):
        return f"The {self.name} car gives the mileage of {self.mileage}km/l."
    
    def max_speed(self,speed):
        return f"The {self.name} car runs at the maximum speed of {speed}km/hr."
    
car1=Car("XUV",30.3)
print(car1.description())
print(car1.max_speed(100))