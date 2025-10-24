
#* Tuples in python
#?  A tuple is an immutable data type in python its indexed , duplicate value allow and its represented by () paranthisis

a = (1,"Monu",45,346,False,"Monu","Ram")
print(type(a))
print(a)

no = a.count("Monu") #? will return number of times "Monu" occurs in a
print(no)

no = a.index(346)  #? wll return the index of first occurrences of 346 in a
print(no)

lenth = len(a)
print(lenth)  #? will return the lenth of the tuple 

my_tuple = (34,2,6,1,56)
print(f"minimum : {min(my_tuple)}")
print(f"maximum : {max(my_tuple)}")


#! Unpacking :-
# ? Tuple can be unpacked into individual varibles
tuples = (2,5,3)
x,y,z = tuples

print(x,y,z)
