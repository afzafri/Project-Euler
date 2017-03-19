listnum = []
for a in range(2,100+1):
	for b in range(2,100+1):
		if (a**b) not in listnum:
			listnum.append(a**b)

listnum.sort()

print len(listnum)