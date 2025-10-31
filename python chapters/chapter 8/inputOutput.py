
#* File i/O in python
#? Python can be used ti perform operations on a file. (read & write data)
# 
#* Types of files
#? 1. Text Files : .txt, .docx, .log etc.
#? 2. Binary Files : .mp4, .mov, .png, .jpeg etc.


# TODO : Open, read & close File
# We have to open a file reading ir writing.
# 
# f = open("file_name","mode")
# 
# file_name :- sample.txt , demo.docx
# mode :- r:read mode , w:write mode
# 
# data = f.read()
# f.close()



# r+ read + overwrite  (pointer stating )  - no truncate
# w+ read + overwrite    - truncate
# a+ read + oappend  (pointer Ending )  - no truncate

# <--------------------------------------------------------------------------------->

# f = open("./demo.txt","r")
# data = f.read(5)
# data = f.read()    # reads entire file
# print(data)         
# line1 = f.readline() # reads one line at a time
# line2 = f.readline()
# print(line1)
# print(line2)


# f = open("demo.txt","w")
# f.write("This is a new line")    #? Overwrite the entire file

# f = open("demo.txt","a")    #? Append 
# f.write("\n after that nodejs")


# f = open("demo.txt","w+")
# f.write("Hello")

# print(f.read())
# f.write("abc")


# f = open("demo.txt","a+")
# print(f.read())
# f.write("abcd")
# f.close()


#!  With syntax

with open("demo.txt","r") as f:
    data = f.read() 
    print(data)


with open("demo.txt","w") as f:
    data = f.write("New data") 
   
