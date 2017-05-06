import math 
import random
from Queue1 import *
from minpriortyqueue import *
time=0
class vertex:
	def __init__(self,name,i):
		self.name=name
		self.i=i
		self.c=""
		self.key=math.inf
		self.p=None


class graph:
	def __init__(self,v,aj):
		self.v=v
		self.aj=aj		

	def prim(self,r):
		r.key=0
		q=priorty(self.v,len(self.v))
		for i in range(0,len(self.v)):
			q.insert(self.v[i])
		while q.empty==False:
			u=q.minimum()
			q.removeminimum()
			for j in range (0,aj[u.i].n):
				w=aj[u.i].mnode(j)
				if w









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
a=random.choice(v)
G.prim(a)		