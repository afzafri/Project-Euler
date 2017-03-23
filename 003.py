import math
number = 600851475143
limit = int(math.sqrt(number)) # generate prime number only up to the square root of the number
not_primenums = set()
prime_facts = set()

# finding prime number, using Sieve of Eratosthenes
for i in range(2,limit+1):
    if i not in not_primenums: 
        if number%i == 0: # check if the prime is factors of the number
        	prime_facts.add(i) 
        for j in range(i*i, limit+1, i):
            not_primenums.add(j) 

print max(prime_facts) # print highest prime factor