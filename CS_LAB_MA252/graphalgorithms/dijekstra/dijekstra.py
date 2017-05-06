import math 
from priortyqueue import *
time=0
class vertex:
	def __init__(self,name,i):
		self.name=name
		self.i=i
		self.d=math.inf
		self.p=None
		
class edge:
	def __init__(self,v,w):
		self.v=v
		self.w=w

class graph:
	def __init__(self,v,aj):
		self.v=v
		self.aj=aj		
	def relax(self,p,u,v,w):
		#print(u.d+w)
		if u.d+w<v.d:
			p.dkey(v.i-1,u.d+w)
			v.p=u

	def dijekstra(self,s):
		s.d=0
		p=priorty(self.v,len(self.v))
		while p.empty()==False:
			u=p.minimum()
			print(u.d)
			p.removeminimum()
			for j in range(0,len(self.aj[u.i])):
				e=self.aj[u.i][j]
				self.relax(p,u,e.v,e.w)
				

v=[]
aj=[]
n=int(input("Enter number of vertices::"))
for i in range (0,n):
	v.append(vertex(input(),i))
	aj.append([])	
m=int(input("Enter number of edges::"))
for i in range (0,m):
	v1,v2,v3 = input("The edge is between and the weight is:: ").split(',')
	#print(v1)
	for j in range (0,n):
		#print(v[j].name)
		if v1==v[j].name:
			#aj[j].append(v2)
			for k in range (0,n):
				if v2==v[k].name:
					aj[j].append(edge(v[k],int(v3)))
G=graph(v,aj)					
G.dijekstra(v[0])