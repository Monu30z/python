
#* function :-
#?             A function is group of statements performing a specific task


# Examle :-
# def avg():
#     a = int(input("Enter your number : "))
#     b = int(input("Enter your number : "))
#     c = int(input("Enter your number : "))
#     average = (a+b+c)/3
#     print(average)

# avg()    



#? factorical

# num = int(input("Enter your number : "))

# fact = 1
# while(num>0):
#     fact = fact*num
#     num-=1
    
    
# print(fact)    

# ? problem 2

# def f_to_c(f):
#     return 5*(f-32)/9

# f = int(input("Enter temperature in F : "))
# c = f_to_c(f)
# print(f"{round(c,2)} °c")

# ? problem 3
# def Sum(n):
#     if(n==1):
#      return 1
  
#     return Sum(n-1) + n

# print(Sum(5))
    
# ? problem 4 pattern printing

# num = int(input("Enter a number : "))

# for i in range(num,0,-1):
#     for j in range(1,i+1,):
#         print("*",end=" ")
#     print()    


#? problem 4 using recursion 
# def pattern(n):
#     if(n==0):
#         return
#     print("*"*n)
#     pattern(n-1)

# pattern(4)


#? problem 4 using recursion
# def inch_to_cms(inch):
#     return inch *2.54

# n= int(input("Enter value in inches : "))

# print(inch_to_cms(n))

#? problem 5

# def table(n):
#     for i in range(1,11):
#         print(f"{n} X {i} = {n*i}")

# table(3)