
#? Conditonal Statements in python 

age = int(input("Enter your age "))

if age >18 :
    print("You are above the age of consent")
    print("Good for you")
elif age < 0 :
    print("you are entering an invalid age")  

elif age == 0 :
    print("you are entering 0 which is invalid ")      
else :
    print("You are below the age of consent")   

print("End of program")    