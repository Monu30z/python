
#? problem 1 
# with open("Practice.txt","w") as f:
#     f.write("Hi everyone\nwe are learing File i/O\n")
#     f.write("using java.\nI like programming in java.")


#? problem 2
# with open("Practice.txt","r") as f:
#     data = f.read()
# new_data = data.replace("java","python")
# print(new_data)    

# with open("Practice.txt","w") as f:
#     f.write(new_data)



#? problem 3

word = "learing"
with open("practice.txt","r") as f:
    data = f.read()
    if(data.find(word) != -1):
        print("found")
    else:
        print("not found")   

