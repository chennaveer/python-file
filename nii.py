class student:
	h=2

	def init(self):
		self,h=7

	def my_func(self,k):
		print("hii,i am in the class")
		self.h=k #assigning the value to instance variable
		print(self.h)
o=student()
print(o.h)
o.my_func(0)
o.my_func(3)
o.my_func(5)