import random

d = 0
p = 0

while true:
	r = input("press r to roll,q to quit: ")
	
	if r == 'r':
		d = random.randint(1,6)
		print("you got:",d)
		if d == 6:
			print("congralations,you can play now.")
			break
		else:
			print("roll again,till u get 6.")

while true:
	r = input("press r to roll, q to quit : ")

	if r == 'r':
		d = ranom.randint(1,6)
		print("you got :",d)

		p = p+d
		if p > 100:
			p=p-d
			print("wait till you get", 100-p,"or less.")

		proint("your new poition is :",p)

		if p == 100:
			print("ooohh you won!")
			exit()
		if p == 8:
			p = 37
			print("wow,a ladder.Go to ",p)
			exit()
		if p==13:
			p=64
			print("wow,a ladder.Go to",P)
			exit() 
		if p==40:
			p=68
			print("wow,a ladder.Go to",P)
			exit()	
		if p==76:
			p=97
			print("wow,a ladder.Go to",p)
			exit()
		if p==100:
			print("ooohh you won!")
			exit()
		if p==11:
			p=2
			print("oops sneak is here. go back to",p)
			exit()	
		if p==25:
			p=4
			print("oops sneak is here. go back to,p")
			exit()
		if p==38:
			p=9
			print("oops sneak is here.go back to",p)
			exit()	
		if p==65:
			p=46	
			print("oops sneak is here.go back to",p)
			exit()	
		if p==89:
			p=70
			print("oops sneak is here.go back to",p)
			exit()	
		if p==93:
			p=64
			print("oops sneak is here.go back to",p)
			exit()


		elif r =='q':
			print("Bye!")
			exit()