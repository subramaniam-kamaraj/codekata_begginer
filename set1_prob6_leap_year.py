N=input()			#Enter year in number

if N.isdigit()==True:
	N=int(N)
	if N%4==0:
		if N%100==0:
			if N%400==0:
				print("yes")
			else:
				print("no")
		else:
			print("yes")
	else:
		print("no")
else:
	print("invalid input")
