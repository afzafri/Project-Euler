sum = 0

fibs = []
fibs.append(1)
fibs.append(2)

fib = 0
i = 2

while fib <= 4000000: 
	fib = fibs[i-1] + fibs[i-2]

	if fib % 2 == 0:
		sum = sum + fib

	fibs.append(fib)
	i = i+1

print sum+2

'''
My solution above follows the
usual fibonacci formula, easier
for me to understand.
But below is
more efficient:
F1 = 1
F2 = 2
sumn = 0
x = 0

while x <= 4000000:
	x = F2 + F1
	F1 = F2  
	F2 = x

	if x % 2 == 0:
		sumn = sumn + x

print sumn+2
'''