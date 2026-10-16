set={"apple","banana","orange","cherry","apple",1,2,True,False}    #here true is considered as 1 and false as 0
print(set)
set.add("grape")    #adding an element to the set
print(set)
print(len(set))    #length of the set
print("banana" in set)    #checking if an element is present in the set
print("kiwi" in set)    #checking if an element is present in the set
print("\n")

thisset={"apple","banana","cherry"}
tropical={"mango","pineapple","papaya"}
thisset.update(tropical)    #adding elements from another set
print(thisset)

mylist=["kiwi","orange"]
thisset.update(mylist)    #adding elements from a list
print(thisset)
thisset.remove("banana")    #removing an element from the set
print(thisset)
print("\n")

myset={"apple","banana","cherry"}
x=myset.pop()    #removes a random element from the set
print(x)
print(myset)
print("\n")

set1={"a","b","c"}
set2={"a",1,2,3}
set3=set1.union(set2)    #joining two sets
print(set3)
set4=set1.intersection(set2)    #finding common elements in two sets
print(set4)
set5=set1.difference(set2)    #finding elements in set1 but not in set2
print(set5)
set6=set2.difference(set1)    #finding elements in set2 but not in set1
print(set6)
set7=set1.symmetric_difference(set2)    #finding elements in set1 or set2 but not in both
print(set7)

