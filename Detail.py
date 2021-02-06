class Student:
    
    def __init__(self,name,date):
        self.name = name
        self.date = date
        
    def detail(self):
        return f'''------------------------------------------------
\t Name is {self.name}.
\t Date of Birth : {self.date}''' 
    
    def city(self,ct):
        return f"\t Lives in {ct} "
    
stud = Student(input('Enter Your Name: '),input('Enter Birthdate : '))
ct = stud.city(input('Enter City : '))
print(stud.detail())
print(ct)