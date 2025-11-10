#?  class :- class is a blueprint for creating objects.

# creating class

# class student:
#     name = "Monu Singh"

# creating object (instance)

# s1 = student()
# print(s1.name)

#<------------------------------------------------------------------------------>

#? __init__function

#? Constructor :- All classes have a function called __init__(), which is always executed when the object is being intiated.

# class Student:
#     name = "Monu"
#     def __inti__(self):
#         print("adding new student in db")


# s1 = Student()

# * A python class is a group of attribute and methods .

# ? class creating 

#* class class_Name():
#*       statements   



# class Students:
#     def __init__(self,name ,age):
#         self.name= name
#         self.age= age


#     def show(self):
#         print(self.name)
#         print(self.age)
      


# stu = Students("monu",34)

# stu.show()



# class Moblie:
#     name = "monu"            #? class variable  
#     def __init__(self ):
#         self.model = "realme"     #? instance variable  

#     def Show_model(self,p):
#         self.price = p   
#         print(f"Model no : {self.model} price is : {self.price} ")

# Mob = Moblie()
# print(Mob.name)
# Nokia = Moblie("nokia 3310")
# Nokia.Show_model(2500)         
# Oppo = Moblie("oppo reno6 5g")
# Oppo.Show_model(25000)         
# Maxx = Moblie("Maxx 07")
# Maxx.Show_model(100000)         

# realme = Moblie()
# print(realme.model)        

# print(id(Nokia))

#? <============================================================================


# class Mobile :
#     fb = "yes"
#     def __init__(self):
#         self.model = "realme"
#     def showModel(self):
#         print(self.model)

#     @classmethod   
#     def show(cls):
#         print(cls.fb)

# realme = Mobile()
# realme.showModel()
# realme.show()


class Mobile :
    fb = "yes"
    def __init__(self):
        self.model = "realme"
    def showModel(self):
        print(self.model)

   

realme = Mobile()
realme.showModel()
print(Mobile.fb)         