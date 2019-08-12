# calculate the power of N wit given exponent (k)

N=input()
k=input()

if N.isdigit()==True and k.isdigit()==True:
	N=int(N)
	k=int(k)
	cal=N**k              #in python ** operator is used for power
	print(cal)
else:
	print("invalid input")
