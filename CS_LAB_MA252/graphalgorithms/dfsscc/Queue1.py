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


	def isempty(self):
		if self.n==0:
			return 1
		else :
			return 0	

	def qprint(self):
		trav=self.head
		while trav!=None:
			return(trav.data)
			trav=trav.pointer

	def mnode(self,m):
		c=0
		trav=self.head
		if m<self.n:
			while trav!=None and c<m:
				trav=trav.pointer
				c=c+1
			return trav.data	
			
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

