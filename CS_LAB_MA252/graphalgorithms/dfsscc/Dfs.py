import math 
from Queue1 import *
time=0
class vertex:
	def __init__(self,name,i):
		self.name=name
		self.i=i
		self.dt=0
		self.ft=0
		self.c=""
		self.d=math.inf
		self.p=None

	def print(self):
		print(self.name,self.dt,self.ft,self.p.name)

class graph:
	def __init__(self,v,aj):
		self.v=v
		self.aj=aj
	def print(self):
		n=len(self.v)
		for i in range (0,n):
			if self.v[i].p!=None:
				self.v[i].print()
			else:
				print(self.v[i].name,self.v[i].dt,self.v[i].ft,"No parent")	
		#for i in range (0,n):	
		#	x=self.aj[i].qprint()
		#	x.print()

	def dfs(self):
		n=len(self.v)
		for i in range(0,n):
			self.v[i].c="white"
			self.v[i].p=None

		for i in range(0,n):
			if self.v[i].c=="white":
				self.dfs_visit(v[i])	


	def dfs_visit(self,u):
		global time
		time=time+1
		u.dt=time
		u.c="gray"
		for j in range (0,aj[u.i].n):
				w=aj[u.i].mnode(j)
				if w.c=="white":
					w.p=u
					self.dfs_visit(w)
		u.c="black"
		time=time+1
		u.ft=time			

v=[]
aj=[]
n=int(input("Enter number of vertices::"))
for i in range (0,n):
	v.append(vertex(input(),i))
	aj.append(queue())	
m=int(input("Enter number of edges::"))
for i in range (0,m):
	v1,v2 = input("The edge is between:: ").split(',')
	#print(v1)
	for j in range (0,n):
		#print(v[j].name)
		if v1==v[j].name:
			#aj[j].append(v2)
			for k in range (0,n):
				if v2==v[k].name:
					aj[j].enqueue(v[k])

	for j in range (0,n):
		#print(v[j].name)
		if v2==v[j].name:
			#aj[j].append(v2)
			for k in range (0,n):
				if v1==v[k].name:
					aj[j].enqueue(v[k])
G=graph(v,aj)
G.dfs()
G.print()	