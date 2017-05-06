class Node:
	def __init__(self,data,color):
		self.key=data
		self.color=color
		self.left=None
		self.right=None
		self.parent=None

class RBtree:
	def __init__(self):
		self.root=None
		self.nil=None


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

	def lrotation(self,x):

		y=x.right
		x.right=y.left
		if y.left!=self.nil:
			y.left.parent=x

		y.parent=x.parent
		if x.parent==self.nil:
			self.root=y	
		elif x==x.parent.left:	
			x.parent.left=y
		else:	
			x.parent.right=y

		y.left=x
		x.parent=y


	def rrotation(self,x):

		y=x.left
		x.left=y.right
		if y.right!=self.nil:
			y.right.parent=x

		y.parent=x.parent
		if x.parent==self.nil:
			self.root=y	
		elif x==x.parent.right:	
			x.parent.right=y
		else:	
			x.parent.left=y

		y.right=x
		x.parent=y




	def fixinsert(self,z):

		while z.parent.color==1:

			if z.parent==z.parent.parent.left:

				uncle=z.parent.parent.right

				if uncle.color==1:
					z.parent.color=0
					uncle.color=0
					z.parent.parent.color=0
					z=z.parent.parent

				else:

					if z==z.parent.right:
						z=z.parent
						self.lrotation(z)	

					z.parent.color=0
					z.parent.parent=1
					self.rrotation(z.parent.parent)		

			else:
				uncle=z.parent.parent.left

				if uncle.color==1:
					z.parent.color=0
					uncle.color=0
					z.parent.parent.color=1
					z=z.parent.parent

				else:

					if z==z.parent:
						z=z.parent
						self.lrotation(z)	

					z.parent.color=0
					z.parent.parent=1
					self.rrotation(z.parent.parent)		



	def rbinsert(self,k):
		y=self.nil
		x=self.root
		z=Node(k,1)
		while x != self.nil:
			y=x
			if z.key<x.key:
					x=x.left
			else:
					x=x.right
		z.parent=y
		if y==self.nil:
			self.root=z
			
		elif z.key<y.key:
			y.left=z

		else:
			y.right=z                        		

		z.left=self.nil
		z.right=self.nil
		z.color=1
		self.fixinsert(z)




	def transplant(self,u,v):

		if u.parent == self.nil:
			self.root=v

		elif u==u.parent.left:
			u.parent.left=v
		else :
			u.parent.right=v

		v.parent=u.parent         


 
	def fixdelete(self,x):
		while x!=self.root and x.color==0:
			if x==x.parent.left:
				w=x.parent.right

				if w.color==1:
					w.color=0
					x.parent.color=1
					self.lrotation(x.parent)
					w=x.parent.right

				elif w.left.color==0 and w.right.color==0:
					w.color=1
					x=x.parent

				elif w.right.color==0:
					w.left.color=0
					w.color=1
					self.rrotation(w)
					w=x.parent.right
					w.color=x.parent.color
					x.parent.color=0
					w.right.color=0
					self.lrotation(x.parent)
					x=self.root


				else:
							
					w.color=x.parent.color
					x.parent.color=0
					w.right.color=0
					self.lrotation(x.parent)
					x=self.root

			else:
				w=x.parent.left
				if w.color==1:
					w.color=0
					x.parent.color=1
					self.rrotation(x.parent)
					w=x.parent.left

				if w.right.color==0 and w.left.color==0:
					w.color=1
					x=x.parent

				elif w.left.color==0:
						w.left.color=0
						w.color=1
						self.lrotation(w)
						w=x.parent.left	
						w.color=x.parent.color
						x.parent.color=0
						w.left.color=0
						self.rrotation(x.parent)
						x=self.root	


				else:		
					w.color=x.parent.color
					x.parent.color=0
					w.left.color=0
					self.rrotation(x.parent)
					x=self.root			
		x.color=0		





	def rbdelete(self,k):

		z=self.search(k)
		y=z 
		yocolor=y.color
		if z.left == self.nil:
			x=z.right
			self.transplant(z,z.right)
		elif z.right==self.nil:
			x=z.left
			self.transplant(z,z.left)
		else:
			y=self.minimum(z.right)
			yocolor=y.color
			x=y.right
			if y.parent==z:
				x.parent=y
			else:	
				self.transplant(y,y.right) 
				y.right=z.right
				y.right.parent=y
			self.transplant(z,y)
			y.left=z.left
			y.left.parent=y
			y.color=z.color
		if yocolor==0:	
			self.fixdelete(x)		



	def inorder(self,r):
		if r is self.nil:
				pass
		if r is not self.nil:
			self.inorder(r.left)
			print(r.key,r.color)
			self.inorder(r.right)

	





#node1=Node(0,1)
#node2=Node(0,1)
t=RBtree()
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
			t.rbinsert(n)
		print("The values inserted in sorted order are:::")	        
		t.inorder(t.root)
	elif c==2:
		print("Enter the value to delete")
		d=int(input())
		t.rbdelete(d)
		print("The remaining values in sorted order are:::")
		t.inorder(t.root)
	
	else:
		print("wrong case input::")
