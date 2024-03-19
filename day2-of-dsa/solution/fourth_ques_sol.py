def isprime(num):
    for i in range(2,num-1):
        if num%i==0:
            return False
    return True
# print(isprime(8))

prime_list=[]
for i in range(2, 100):
    if isprime(i):
        prime_list.append(i)
    else:
        pass
print(prime_list)