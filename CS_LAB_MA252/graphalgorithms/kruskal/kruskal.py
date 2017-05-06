import math
import sys
import operator
import random
import string
time=0

class vertex:
	def __init__(self,name,i):
		self.p=None
		self.i=i
		self.rank=0
		self.name=name

	def makeset(self):
		self.p=self
		self.rank=0

	def union(self,x):
		self.findset().link(x.findset())

	def link(self,x):	
		if self.rank>x.rank :
			x.p=self
		else:
			self.p=x
			if self.rank==x.rank :
				x.rank=x.rank+1	

	def findset(self):
		if self!=self.p:
			self.p=self.p.findset()
		return self.p			
		
class edges:
	def __init__(self,name,weight):
		self.name=name
		self.weight=weight

class Graph:
	def __init__(self,v,e):
		self.v=v
		self.e=e

	def kruskal(self):	
		#newlist=[]
		self.e.sort(key=operator.attrgetter('weight'))
		#newlist=sorted(self.e,key=operator.attrgetter('weight'))
		for i in range (0,len(self.v)):
			self.v[i].makeset()	
		for i in range(0,len(self.e)):
			u,w=self.e[i].name.split(",")
			for j in range (0,int(n)):
				if u==self.v[j].name:
					break
			for k in range (0,int(n)):
				if w==self.v[k].name:
					break			
			#print(u,w)		
			if self.v[j].findset()!=self.v[k].findset():
				print(u,w)
				self.v[j].union(self.v[k])

#INPUT YOURSELF
'''
v=[]
e=[]
str=""
n=int(input("Enter number of vertices::"))
for i in range (0,n):
	v.append(vertex(input(),i))
m=int(input("Enter number of edges::"))
for i in range (0,m):
	str=input("The edge is between and the weight is::")
	v1,v2,v3=str.split(",")
	e.append(edges(v1+","+v2,int(v3)))
G=Graph(v,e)
G.kruskal()



'''#INPUT RANDOMLY
def randomword(length):
   return ''.join(random.choice(string.ascii_lowercase) for i in range(length))


n=sys.argv[1]
m=sys.argv[2]
a=[]
for i in range (0,int(n)):
	v.append(vertex(randomword(3),i))
for i in range (0,int(n)):
	a.append(v[i].name)
for i in range (0,int(m)):
	v1=random.choice(a)
	v2=random.choice(a)
	v3=random.randint(0,1000)
	e.append(edges(v1+","+v2,int(v3)))
G=Graph(v,e)
G.kruskal()