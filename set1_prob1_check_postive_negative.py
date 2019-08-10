N = input()

if N.isdigit() and N=='0':
	print("Zero")
elif N.isdigit() and N>'0':
	print("Positive")
elif N[0]=='-' and N[1:].isdigit():
	print("Negative")
else:
	print("invalid input")
