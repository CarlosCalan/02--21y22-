def isPrime(numb):
    
    if numb<=0 or numb==1:
        return False
    if numb==2:
        return True
    for i in range(2,numb):
        a=numb%i
        if a==0:
            return False
        else:
            return True

for i in range(1, 20):
	if isPrime(i + 1):
			print(i + 1, end=" ")
print()

        