# name = input("Enter your name ")

# print("good Afternoon ",name) # if both are string

# print(f"Good afternoon {name}")   

letter = '''Dear <|name|>,
            You are selected!
            <|date|>'''

print(letter.replace("<|name|>" , "Monu").replace("<|date|>","13 july 2025"))



# problem 3  _ find double space

name = "hi, My name is  monu "
print(name.find("  "))

# problem 4 - replace double space with single space

print(name.replace("  ", " "))

#problem 5 - format the following problem using escape charaters 

letter = "Dear Monu,\n\tThis python course is nice.\nThanks!"

print(letter)
