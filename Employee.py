class Employee:
    
    def __init__(self , ename, age):
        self.ename = ename
        self.age = age
        
    def detail(self):
        print(self.ename , self.age)
        
class Emp(Employee):
    
    def __init__(self , ename , age):
        Employee.__init__(self, ename, age)
        self.sal = 15000
        
    def detail(self):
        print("Employee Name : ", self.ename)
        print("Age : ",self.age)
        print("Salary : ",self.sal,"/month")
        
        
emp = Emp('Mr.Patel' , 25)
emp.detail()