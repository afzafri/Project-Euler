sumsq = 0
sumn = 0

for i in range(1,100+1):
	sumsq = sumsq + (i**2)
	sumn = sumn + i

diff = (sumn**2) - sumsq
print diff
