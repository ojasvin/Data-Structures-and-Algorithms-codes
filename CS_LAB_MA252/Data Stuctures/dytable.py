from ctypes import *
class dytable:
	def __init__(self):
		self.curcap=0
		self.maxcap=2
		self.data=(c_int*2)()

	def add(self,x):
		if self.curcap==self.maxcap:
			new=(c_int*(2*self.maxcap))()
			
			for i in range (0,self.curcap):
				new[i]=self.data[i]
			self.data=new
			self.maxcap=2*self.maxcap
			
		self.data[self.curcap]=x
		self.curcap=self.curcap+1

	def delete(self):
		self.curcap=self.curcap-1
		if self.curcap==int((self.maxcap)*0.25):
			new=(c_int*(int(0.5*self.maxcap)))()
			for i in range (0,self.curcap):
				new[i]=self.data[i]
			self.data=new	
			self.maxcap=int(0.5*self.maxcap)


arr=dytable()
print("Enter no of elements to be added")
n=int(input())
for i in range (0,n):
	m=int(input())
	arr.add(m)
	
print("The elements are::")	
for i in range (0,arr.curcap):
	print(arr.data[i])	

print("The current size::") 	
print(arr.curcap)
print("Enter no of elements to be deleted")
n1=int(input())
if n1>n:
	print("error:")
else:
	for i in range (0,n1):
		arr.delete()
	
print("The elements are::")		
for i in range (0,arr.curcap):
	print(arr.data[i])
	
print("The current size::") 	
print(arr.curcap)
