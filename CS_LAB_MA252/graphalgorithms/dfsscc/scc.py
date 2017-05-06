import math
import operator
from Queue1 import *
time=0
class vertex:
	def __init__(self,name,i):
		self.name=name
		self.i=i
		self.dt=0
		self.ft=0
		self.c=""
		self.p=None

	def print(self):
		print(self.name,self.dt,self.ft,self.p.name)

class Time():
	def __init__(self,v,ft):
		self.v=v
		self.ft=ft
		
class graph:

	def __init__(self,v,aj):
		self.v=v
		self.aj=aj

	def scc(self):
		self.dfs()
		for i in range(0,len(self.v)):
			u=self.v[i]
			for j in range (0,self.aj[u.i].n):
				w=self.aj[u.i].mnode(j)
				aj2[w.i].enqueue(u)

		G2=graph(self.v,aj2)		
		G2.dfs2()		

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


	def dfs2(self):
		n=len(self.v)
		ass=[]
		for i in range(0,n):
			ass.append(Time(self.v[i],self.v[i].ft))
		for i in range(0,n):
			self.v[i].c="white"
			self.v[i].p=None
		
		ass.sort(key=operator.attrgetter('ft'),reverse=True)	
	
		for i in range(0,n):
			if ass[i].v.c=="white":
				self.dfs_visit2(ass[i].v)
				print()

	def dfs_visit2(self,u):
			print(u.name,end=' ')
			u.c="gray"
			for j in range (0,aj2[u.i].n):
				w=aj2[u.i].mnode(j)
				if w.c=="white":
					w.p=u
					self.dfs_visit2(w)
			u.c="black"
		

v=[]
aj=[]
aj2=[]
n=int(input("Enter number of vertices::"))
for i in range (0,n):
	v.append(vertex(input(),i))
	aj.append(queue())	
	aj2.append(queue())
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
'''
	for j in range (0,n):
		#print(v[j].name)
		if v2==v[j].name:
			#aj[j].append(v2)
			for k in range (0,n):
				if v1==v[k].name:
					aj[j].enqueue(v[k])
'''
G=graph(v,aj)					
G.scc()