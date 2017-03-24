lim = 1000000
sum = 0

for i in range(1,lim+1):
	if (i == int(str(i)[::-1])) and (int(bin(i)[2:]) == int(bin(i)[2:][::-1])):
		sum = sum + i

print sum