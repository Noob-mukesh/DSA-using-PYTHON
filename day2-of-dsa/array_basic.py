import array
l1=array.array("i",[1,2,4,8])
print(l1)
for i in l1:
    print(i)
# convert array into list
to_list=l1.tolist()
print(to_list)
# convert array into byte
print(l1.tobytes())

# find type code of array
print(l1.typecode)

# give buffer info>>>> location  and length of array
print(l1.buffer_info())

#  find item size

print(l1.itemsize)
# 
# print(l1.tofile(open('abc.txt','wb')))
# read from file to 

print(l1.byteswap())
# creatng array of floating type value
l5=array.array("f",[10.0,6,0])
print(l5)

# will give error if we insert no-floating value
l5=array.array("f",[10.0,6,0,"hi"]) #TypeError: must be real number, not str
print(l5)