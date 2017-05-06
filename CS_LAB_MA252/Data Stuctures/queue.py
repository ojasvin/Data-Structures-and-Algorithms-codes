class Node:
	def __init__(self):
		self.data=None
		self.pointer=None 

class queue:
	def __init__(self):
		self.n=0
		self.head=None
		self.tail=None

	def enqueue(self,x):
		temp=Node()
		temp.data=x
		if self.n==0:
			self.head=temp
			self.tail=temp
			self.n+=1
		else:
			self.tail.pointer=temp
			self.tail=temp
			self.n+=1

	def dequeue(self):
		if self.n==0:
			raise ValueError("Queue is empty")
			return
		
		element=self.head.data
		self.head=self.head.pointer
		self.n=self.n-1
		return element

	def qprint(self):
		trav=self.head
		while trav!=None:
			print(trav.data)
			trav=trav.pointer


	def search(self,x):
		trav=self.head
		f=0
		while trav!=None:
			if trav.data==x:
				print("Found::")
				f=1
				break
			trav=trav.pointer	
		if f==0:
			print("not found::")


q=queue()
for i in range (0,10):
	q.enqueue(int(input()))
print("output")	
q.qprint()	
q.search(12)
for i in range (0,5):
	q.dequeue()
print("output2")		
q.qprint()
q.search(12)	