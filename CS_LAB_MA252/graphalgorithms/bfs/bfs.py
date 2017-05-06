import math
from Queue import *
class vertex:

	def __init__(self,name,i):
		self.name=name
		self.i=i
		self.c=""
		self.d=math.inf
		self.p=None

	def print(self):
		print(self.name,self.c,self.d,self.p)

class graph:
	def __init__(self,v,aj):
		self.v=v
		self.aj=aj

	def print(self):
		n=len(self.v)
		#for i in range (0,n):
		#	self.v[i].print()
		for i in range (0,n):	
			x=self.aj[i].qprint()
			x.print()
	def bfs(self,source):
		n=len(self.v)
		for i in range (0,n):
			if self.v[i].name!=source:
				self.v[i].c="white"
				self.v[i].p=None
				self.v[i].d=math.inf		
			else:
				sindex=i
				self.v[i].c="grey"
				self.v[i].p=None
				self.v[i].d=0	

		Q=queue()
		#w=vertex("",0)
		Q.enqueue(self.v[sindex])
		while Q.isempty()==0 :
			u=Q.dequeue()
			u.print()
			#print(aj[u.i].n)
			
			for j in range (0,aj[u.i].n):
				w=aj[u.i].mnode(j)
				#print(w.c)
				#w.print()
				if w.c=="white":
					w.c="gray"
					w.d=u.d+1
					w.p=u
					Q.enqueue(w)
				#Q.qprint()	
				#w.print()	
			u.c="black"			

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

s=input("Enter source::")
G.bfs(s)		
#G.print()









