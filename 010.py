# using Sieve of Eratosthenes, can be optimize more
limit = 2000000
# set objects is more faster
not_primenums = set()
sum = 0

for i in range(2,limit+1):
    if i not in not_primenums:
        sum = sum + i # sum
        for j in range(i*i, limit+1, i):
            # store multiple of the prime in here (not prime)
            not_primenums.add(j) 

print sum
