class Parent:
    
    def __init__(self , fname, fage):
        self.firstname = fname
        self.age = fage
        
    def view(self):
        print(self.firstname , self.age)
        
class Child(Parent):
    
    def __init__(self , fname , fage):
        Parent.__init__(self, fname, fage)
        self.lastname = "VP and DP's Class"
        
    def view(self):
        print("Course" , self.firstname ,"first came", self.age , " years ago." , self.lastname, "has courses to master python")
        
        
obj = Child('Python' , '28')
obj.view()