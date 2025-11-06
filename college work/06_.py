
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


def disp():
    def show():
        return "show function"
    
    result = show() + "disp function" 
    return result
  
a= disp()
print(a)

