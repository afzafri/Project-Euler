fibs = []
fibs.append(1)
fibs.append(1)

i = 2

while True:
	fib = fibs[i-1] + fibs[i-2]

	if(len(str(fib)) == 1000):
		print "index: " + str(i+1)
		break

	fibs.append(fib)
	i = i+1