new_li=[]
def remove_non_int(args):
    
    "remove non int value from list"
    for i in args:
        if type(i) == int:
            new_li.append(i)
    return new_li

orignal_list= ["hi", "helloo",1,3,7.0,1j,True,False,None,["hui"],{1},{"hi":1}]

# print(remove_non_int(orignal_list))
