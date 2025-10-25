
#? problem 1  
# num = int(input("Enter a number "))

# for i in range(1,11):
#     print(i*num)
#     i+=1

#? problem 2

# l = ["harry","sonam","sachin","Rahul"]

# for name in l:
#     if(name.startswith("s")):
#         print(f"Hello {name}")

#? problem 3 

# num  = int(input("Enter a number : "))

# i=1
# while(i<11):
#     print(num*i)
#     i+=1

#? Problem 4

# num = int(input("Enter a number : "))
# for i in range(2,num):
#     if(num%i)==0:
#         print(f"{num} not a prime number")
#         break
#     else:
#         print(f"{num} is a prime number")   
#         break
       

#?  problem 5

num = int(input("Enter a number "))
i=0
sum = 0
while(i<num):
    sum+=i
    i+=1
print(sum)    