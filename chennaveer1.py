def largest(a,b,c):
	if a>=b and a>=c :
		return(a)
	elif b>=c	and b>=a :
		return(b)
	else:
		return(c)
d=largest(3,4,9)
print(d)

