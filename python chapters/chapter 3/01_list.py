
# * what iw list 
# ? list is a collection of data element in which elements are organiced , indexed , allow duplicate values and mutable. it is represented by [] subscript.


# example 

friends = ["apple","orange", 5,345.54,False,"monu","Rama"]
print(friends[0])
friends[0] = "banana"
print(friends[0])


# * insertion in list
 
friends.append("gpmau")

print(friends)

l1 = [1,2,4,6,8,4,2]
print(l1)
l1.insert(3,10)  #? this will add 10 at 3 index
print(l1)

l1.pop(3)  #? will delete elment at index 2 and retuurn its value
print(l1)

l1.remove(2)  #? wll remove first 2 from the list
print(l1)






