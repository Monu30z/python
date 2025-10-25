
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

num = int(input("Enter your number : "))

fact = 1
while(num>0):
    fact = fact*num
    num-=1
    
    
print(fact)    
