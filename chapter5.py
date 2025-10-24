#📌📌  list

frinds = ["apple" , "Orenge" ,5, 54.3 , False,"monu ", "shashank"]
print(type(frinds))

print(frinds[0])
print(frinds[5])
print(frinds[3])


frinds[0] = "yo yo"
print(frinds[0])   # list are mutable 
print(frinds[1 : 4])
# frinds.append("Mahi")
# print(frinds)

# Lists Methods 
num = [2,5,7,3,6,2,7,7,8,3,1,4,6]

print(num)
num.sort()
print(num)
num.reverse()
print(num)

num.insert(6,777)   #   num.insert(index,number)
print(num)

num.pop()   #  remove elements from last sides
num.pop()
num.pop(3)   # num.pop(index)  => index number which you want to remove
print(num)

num.remove(777)  # num.remove(element)
print(num)

