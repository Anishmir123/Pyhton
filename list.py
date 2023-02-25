#list3=[] #empty list

list1=["rahul",21,"male","surej",22,"male"]

#list several method
#count
print(list1.count("rahul"))

#index (The index() method returns the position at the first occurrence of the specified value.)

print(list1.index(21))

#insert

list1.insert(5,"saiyad")
print(list1)

#pop{The pop() method removes the element at the specified position or index}

list1.pop(5)
print(list1)

#extend{The extend() method adds the specified list elements (or any iterable) to the end of the current list}

#list2=["naggo","muli"]
#list1.extend(list2)
#print(list1)

#copy {The copy() method returns a copy of the specified list}

list3=list1.copy()
print(list3)

#sort {The sort() method sorts the list ascending by default}
list4=[45,78,23,33,89]
#list4.sort() //by default asending order
list4.sort(reverse=True)#Decending  order
print(list4)

#reverse

list4.reverse()
print(list4)







