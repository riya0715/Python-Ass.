class Parent:
    
    def func1(self):
        print('This is Parent class’s function')
        
class Child(Parent):
    
    def func2(self):
        print('This is Child class’s function')
        
obj=Child()
obj.func1()
obj.func2()