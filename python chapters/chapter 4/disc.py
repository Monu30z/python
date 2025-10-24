
#* Dictionary 
#? Dictionary is a collection of key value pairs. it is unorderd . mutable , indexed and duplicate values are not allowed.

a = {
    "name":"Monu",
    "branch" : 'CES',
    "marks": 33,
    "lists":[1,2,3]
} 

# print(a["name"])
# print(a["lists"])

#* b=a.items() 
#? returns a list of (Key,value) tuples.
#* print(b)
#* print(a.keys())
 #? returns a list containing dictionary's Keys

#* a.update({"marks":55})
    #?: Updates the dictionary with supplied key-value pairs.

#* print(a)  
#? marks = 55


#* print(a.get("name"))
#? Returns the value of the specified keys (and value is returned eg."Monu" is returned here).





#!  Sets 
#? Set is a collectionof non-repetittive elements. it's unorderd,unindexed
#?  There is no way to change items in sets. and sets connot contain duplicate values.

#* it's represented by {} `curly bracket`

# s = set() #*empty set
# s = {1,8,2,3,True}

# print(len(s))

# s.add(566)
# print(s)

# for x in s:
#     print(x)


# print(8 in s)

# v = {"rama","Monu","vijay"}

# s.update(v)
# print(s)



# mylist = ["raja","aman","raju"]

# s.update(mylist)
# print(s)

# ? TO remove an item in a set use the remove() or the discard()  method

# ? remove a rendom item by using the pop() method

# s.remove(8)
# print(s)



#* Union

set1 = {1,2,3}
set2 = {"a","b","c",1}

# set3 = set1.union(set2)
# set3 = set1.intersection(set2)

set1.intersection_update(set2)
print(set1)

