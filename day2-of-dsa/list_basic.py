#  create an empty list
l1=[]
print(l1)
#  create  a list with some elements
l2=[1,2,3,4,0]

print(l2)
# adding  element to the end of the list
l2.append(8)
print(l2)
# remove last element
l2.pop()
print(l2)
#  remove element by index
l2.remove(1)
print(l2)


# sorting
l2.sort()
print(l2)
# reverse list
l2.sort(reverse = True)
print(l2)

#  add another list in same list
l2.extend([10,29])
print(l2)

# shallow copy of list
l3=l2.copy()
print(l3)
print(id(l3))
print(id(l2))

# count how many  times an element is present in the list
x=l3.count(10)
print(x)

# find index of an element
c=l3.index(0)
print(c)
# reverse list
l3.reverse()
print(l3)

# insert  element at specific position
l3.insert(3,"mukesh")
print(l3)

# remove element by name
l3.remove("mukesh")
print(l3)

# remove all element from list
l3.clear()
print(l3)

