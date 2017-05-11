class cqueue:

	def __init__(self,size):
		self.front=0
		self.rear=-1
		self.arr=[None]*size
		self.size=size
		self.count=0

	def insert(self,x):
		if self.count==self.size:
			print("full")
		else:
			self.rear=(self.rear+1)%self.size
			self.arr[self.rear]=x
			self.count=self.count+1	

	def delete(self):
		if self.count==0:
			print("empty")
		else:			
			self.front=self.front+1
			self.count=self.count-1		

	def print(self):
		c=self.count
		i=0
		while c!=0:
			print(self.arr[(self.front+i)%self.size])
			i=i+1
			c=c-1

q=cqueue(5)
q.insert(5)
q.insert(10)
q.insert(9)
q.insert(7)
q.delete()
q.delete()
q.insert(99)
q.insert(11)
q.insert(23)
q.insert(33)
q.print()		


