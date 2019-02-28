import random
l=["r","p","s"]
d={'r':"rock",'p':"paper",'s':"siceor"}
us=0
cs=0
while True:
	#take input from usear
	u=input("enter ur choice,press n to dis continue")
	#to exit
	if u=='n':
		print("game over")
		print("computer score:",cs)
		print("usear score:",us)
		if cs==us:
			print("tie")
		elif cs > us:
			print("computer wins")
		else:
			print("usear wins")
		exit()
	
	#input from computer
	c=random.choice(l)
	print("computer chooses:",d[c])
	print("usear chooses:",d[u])

	#copare the user and computer choice
	if u == c:
		print("tie")
	elif u=="r" and c=="p":
		print("comp wins")
		cs=cs+1
	elif u == "r" and c =="s":
		print("usear wins")
		us=us+1
	elif u == "p" and c == "r":
		print("comp wins")
		cs=cs+1
	elif u == "p" and c == "s":
		print("usear wins")
		us=us+1
	elif u == "s" and c == "r":
		print("comp wins")
		cs=cs+1
	elif u == "s" and c == "p":
		print("usear wins")
		us=us+1