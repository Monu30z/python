# def greet(name):
#     print(f"Good Day {name}")

# greet("Monu")    
# greet("Rama")    
# greet("john")    



# def fun(name):
#     greet = "hey " + name
#     return greet

# print(fun("monu"))


#?  function with default argument value 

# def greet(name="User"):
#     print(f"wallcome {name}") 

# greet("Rama")    
# greet()    


#?   function with variable length arguments use *arg  or   **arg

# def sums(*args):
#     result = 0
#     for num in args:
#         result+=num
#     return result    

# print(sums(2,4,2))    
# print(sums(9,6,5,9,2))    



#? function returing multiple values

# def calculate(a,b):
#     sum = a+b
#     diff = a - b

#     return sum,diff

# # print(calculate(4,2))
# result = calculate(4,2)
# print(f"sum : {result[0]}")
# print(f"diff : {result[1]}")