num = 2**1000
listnum = list(str(num))

sum = 0
for i in range(len(listnum)):
	sum = sum + int(listnum[i])

print sum