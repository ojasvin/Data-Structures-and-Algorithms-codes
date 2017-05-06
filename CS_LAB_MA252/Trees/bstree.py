class Node:
	def __init__(self,data):
		self.key=data
		self.left=None
		self.right=None
		self.parent=None

class Bstree:
	def __init__(self):
		self.root=None

	def search (self,k):
		x=self.root
		while x!=None and k!=x.key:
			if k<x.key:
				x=x.left
			else:
				x=x.right   
		return x        

	def minimum (self,x):
		while x!=None:
			y=x
			x=x.left
		return y  


	def maximum (self,x):
		while x!=None:
			y=x
			x=x.right
		return y


	def insert(self,k):
		y=None
		x=self.root
		z=Node(k)
		while x != None:
			y=x
			if z.key<x.key:
					x=x.left
			else:
					x=x.right
		z.parent=y
		if y==None:
			self.root=z
		elif z.key<y.key:
			y.left=z
		else :
			y.right=z                          


	def transplant(self,u,v):
		if u.parent == None:
			self.root=v

		elif u==u.parent.left:
			u.parent.left=v
		else :
			u.parent.right=v
		if v!=None:
			v.parent=u.parent         
 


	def delete(self,k):
		z=self.search(k) 
		if z!=None:
			if z.left == None:
				self.transplant(z,z.right)
			elif z.right==None :
				self.transplant(z,z.left)
			else:
				y=self.minimum(self.root.right)
				if y.parent!=z:
					self.transplant(y,y.right) 
					y.right=z.right
					y.right.parent=y
				self.transplant(z,y)
				y.left=z.left
				y.left.parent=y
		else:
			print("not present::")		



	def inorder(self,r):
		if r is None:
				pass
		if r is not  None:
			self.inorder(r.left)
			print(r.key)
			self.inorder(r.right)


node1=Node(0)
node2=Node(0)
t=Bstree()
print("enter number of cases::")
v=int(input())
print("1 for input\n 2 for delete \n 3 for max and min \n 4 for searching")
for j in range (0,v):
	print("enter case::")
	c=int(input())
	if c==1:
		print("Enter nof of values to be inserted::")
		m=int(input())
		for i in range (0,m):
			print("Enter value::")
			n=int(input())
			t.insert(n)
		print("The values inserted in sorted order are:::")	        
		t.inorder(t.root)
	elif c==2:
		print("Enter the value to delete")
		d=int(input())
		t.delete(d)
		print("The remaining values in sorted order are:::")
		t.inorder(t.root)
	elif c==3:
		node1=t.maximum(t.root)
		print("The maximum is:::",node1.key)
		node2=t.minimum(t.root)
		print("The minimum is:::",node2.key)
	elif c==4:
		print("Enter value to be searched")
		r=int(input())	
		node1=t.search(r)
		if node1!=None:
			print("found")
		else:
			print("not found")

	else:
		print("wrong case input::")
			
