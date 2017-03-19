i = 100
res = 1
while i >= 1:
	res = res * i
	i = i - 1

listnum = list(str(res))

sum = 0

for i in range(len(listnum)):
	sum = sum + int(listnum[i])

print sum
