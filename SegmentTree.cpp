#include<bits/stdc++.h>
using namespace std;
int rangequery(int ql, int qr, int *seg,int n)
{
	int res=0;
	for(ql+=n,qr+=n;ql<qr;ql=ql>>1,qr=qr>>1)
	{
		if(ql&1)
			res+=seg[ql++];
		if(qr&1)
			res+=seg[--qr];

	}
	return res;

}
void updatevalue(int a[],int n, int index, int val, int *seg)
{
	a[index]=val;
	int i;
	seg[n+index]=val;
	index=n+index;
	for(i=index;i>0;i=i>>1)
	{
		seg[i>>1]=seg[i]+seg[i^1];
	}
}

void buildTree(int a[],int n, int *seg)
{
	int i;
	for(i=0;i<n;i++)
	{
		seg[n+i]=a[i];
	}
	for(i=n-1;i>0;i--)
	{
		seg[i]=seg[i<<1]+seg[i<<1|1];
	}
	
}
int main()
{
	int n,i;
	cin>>n;
	int a[n];
	for(i=0;i<n;i++)
		cin>>a[i];
	int *seg;
	seg=new int[2*n];
	buildTree(a,n,seg);
	for(i=1;i<2*n;i++)
		cout<<seg[i]<<" ";
	cout<<endl;
	int up,val;
	cin>>up;
	cin>>val;
	updatevalue(a,n,up-1,val,seg);
	for(i=1;i<2*n;i++)
		cout<<seg[i]<<" ";
	cout<<endl;

	int ql,qr;
	cin>>ql;
	cin>>qr;
	cout<<rangequery(ql,qr+1,seg,n)<<endl;
}