# this algo is slow. may not be efficient
primes = set()
i = 2
term = 1
lim = 10001

while True:
	# check if term counts reach 10001 break the loop
	if term > lim: 
		break
	# find primes, if found, increase the term count
	for j in range(2,i): 
		if i%j == 0:
			break
	else:
		primes.add(i)
		term = term + 1 
	i = i + 1

print sorted(primes)[lim-1] # sort the set, and access the 10001th prime
