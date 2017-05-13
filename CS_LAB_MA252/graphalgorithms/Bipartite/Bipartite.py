import math
from main import *
class vertex:

	def __init__(self,name,i):
		self.name=name
		self.i=i
		self.c=""
		self.clas=0
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
	def bfsbipartite(self,source):
		n=len(self.v)
		source.c="grey"
		source.p=None
		source.d=0	
		source.clas=1

		Q=queue()
		#w=vertex("",0)
		Q.enqueue(source)
		while Q.isempty()==0 :
			u=Q.dequeue()
			u.print()
			#print(aj[u.i].n)
			
			for j in range (0,aj[u.i].n):
				w=aj[u.i].mnode(j)
				#print(w.c)
				#w.print()
				if w.c=="white":
				  w.clas=1-u.clas
					w.c="gray"
					w.d=u.d+1
					w.p=u
					Q.enqueue(w)
				#Q.qprint()	
				#w.print()	
			u.c="black"	
			
		for x in (self.v):
		  for j in range(0,aj[x.i].n):
		    w=aj[x.i].mnode(j)
		    if x.clas==w.clas:
		      return 0
    
    return 1 
    
    
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

	
G=graph(v,aj)
for x in G.v:
	if x.c=="white":
		ans=G.bfsbipartite(x)	
		if ans==0:
			break
if ans ==0:
	print("Graph is not bipartite")
else:
	print("Graph is bipartite")	
	print("The Partition is::")
	print("Part 1=",end=" ")
	for x in G.v:
		if x.clas==1:
			print(x.name,end=" ")
	print()
	print("Part 2=",end=" ")	
	for x in G.v:
		if x.clas==0:
			print(x.name,end=" ")
	print()		