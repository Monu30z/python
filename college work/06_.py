
# ? What is function ? 
# :- a function is a block of code that perform a specific task 


# def add():
#     a,b = 10,20
#     c=a+b
#     print(c)

# add()  


# def add():
#     x,y = 10,20
#     z=x+y
#     return z

# print(add())


# def add(y):
#     x=10
#     c= x+y
#     d = x-y
#     e= x*y
#     return(c,d,e)

# sum,sub,mult=add(5)
# print(sum)
# print(sub)
# print(mult)

# def disp():
#     def show():
#         print("show function")
#     print("disp function")
#     show()    


# disp()


# def disp():
#     def show():
#         return "show function"
    
#     result = show() + "disp function" 
#     return result
  
# a= disp()
# print(a)


#?   formal and actual parameter


#?  Recursion


# def myfun():
#     print("gp mau")
#     myfun()
# myfun()    


# def factorial(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*factorial(n-1)
    
# factorial(5)    


# i = 0
# def myfun():
#     global i
#     i=i+1
#     print("my func",i)
#     myfun()
# myfun()    



#*  lambda function 

# x = lambda a,b: (a+b , a-b)
# c,d =x(10,20)
# print(c , d) 


#* <------------------------------->              
# x = lambda a,b =20: (a+b , a-b)
# c,d =x(10)
# print(c , d) 

# ?=================================
x = lambda a=10,b =20: (a+b , a-b)
c,d =x()
print(c , d)


