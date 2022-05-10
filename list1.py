l1 = [ ]

l1.append(10) #append method - store the single value in end of the list
print(l1)

l1.extend((22,33,44,55,66)) #Extend method is used to store multiple values at a time and result is store in end of the list

l1.extend((100,200,300,400,5,10,15,25,35,65,75,165))
print(l1)

l1.insert(1,2000) #Insert method is  store the value by specific position
print(l1)

l1.pop(3) #pop method is used to remove the specified indixing
print(l1)

l1.remove(2000) # remove method is used to remove the given value
print(l1)

del l1[4] # del method  is used to remove the value by specified indexing
print(l1)

l1.clear()
print(l1) # clear method is used to clear the entire list and  give the empty list

print(l1.count(55)) #count method display the specified value how many times comes in list

print(l1.index(200))# index method shows the indexing value of specified value 
print("Before sorting",l1)
l1.sort() # sort the list in  asscending order and returns none 
print("After sorting",l1)
l1.reverse() # reverse the list
print(l1)
# #print(dir(l1))