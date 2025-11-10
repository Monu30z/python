z
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



class Students:
    def __init__(self,name ,age):
        self.name= name
        self.age= age


    def show(self):
        print(self.name)
        print(self.age)
      


stu = Students("monu",34)

stu.show()