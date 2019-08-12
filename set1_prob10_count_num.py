N=input()

if N.isdigit()==True:
	N=int(N)
	count=0
	while N>0 :
		N=N//10
		count=count+1
	print(count)	
else:
	print("invalid input")
