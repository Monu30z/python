# class Programmer:
#     company = "Microsoft"
#     def __init__(self,name,age,salary):
#         self.name = name
#         self.age = age
#         self.salary= salary
    
# em1 = Programmer("Ram",23,300000) 
# em2 = Programmer("Mohan",30,3780000) 
# print(em1.name ,em1.age,em1.salary)   
# print(em2.name ,em2.age,em2.salary)   



class Calculator:
    def __init__(self,n):
        self.n = n

    def Square(self):
        print(self.n*self.n)    

    def Cube(self):
        print(f'{self.n*self.n*self.n}')

    def squareroot(self):
        print(self.n**1/2)
        
    @staticmethod
    def Greet():
        print("Hello")    

num = Calculator(4)
num.Greet()

num.Cube()
num.Square()
num.squareroot()