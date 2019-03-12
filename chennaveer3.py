try:
	l=[2,3,4,5]

	s=len(l)
	if l>6:
		raise TypeError
		print (d[7])

except TypeError:
		print("Error!!!!length shold be less than or equals to 5")
except NameError:
		print("index out of range")
else:
	for i in l:
		print(i)
finally:
		print("execution done!!!!")

