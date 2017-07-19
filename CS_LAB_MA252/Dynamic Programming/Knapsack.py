def knapsack01(W,wt,val,n):
	K=[[0 for x in range(W+1)] for y in range(n+1)]
	for i in range(1,n+1):
		for w in range(1,W+1):
			if wt[i-1]<=w:
				K[i][w]=max(val[i-1]+K[i-1][w-wt[i-1]],K[i-1][w])
			else:
				K[i][w]=K[i-1][w]

	return K[n][W]			

def main():
	wt=[]
	val=[]
	n=int(input("Enter the number::"))
	W=int(input("Capacity::"))
	for i in range(0,n):
		st=str(input())
		wt.append(int(st.split()[0]))
		val.append(int(st.split()[1]))

	print(knapsack01(W,wt,val,n))	


if __name__ == '__main__':
	main()