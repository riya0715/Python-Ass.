class Student:
    
    def __init__(self,name,date):
        self.name = name
        self.date = date
        
    def detail(self):
        return f'''Name is {self.name}.
Date of Birth : {self.date}''' 
    
    def city(self,city):
        return f"Lives in {city} "
    
stud = Student("Mr.Patel","11-12-13")
print(stud.detail())
print(stud.city('Anand'))