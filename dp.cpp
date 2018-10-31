#include<bits/stdc++.h>
using namespace std;
vector <int> bruteforce(int price,int coins[])
{
	vector<int> p(4,0),q(4,0),r(4,0),s(4,0);	
	vector<int> ans;
	int t1=0,t2=0,t3=0,t4=0;
	if(price==0)
		return p;
	if(price>=1)
	{
		p=bruteforce(price-1,coins);
		if(p[0]<coins[0])
		{
			p[0]=p[0]+1;
			t1=p[0]+p[1]+p[2]+p[3];
		}
	}
	if(price>=5)
	{
		q=bruteforce(price-5,coins);
		if(q[1]<coins[1])
		{
			q[1]=q[1]+1;
			t2=q[0]+q[1]+q[2]+q[3];
		}
	}
	if(price>=10)
	{
		r=bruteforce(price-10,coins);
		if(r[2]<coins[2])
		{
			r[2]=r[2]+1;
			t3=r[0]+r[1]+r[2]+r[3];
		}
	}
	if(price>=25)
	{
		s=bruteforce(price-25,coins);
		if(s[3]<coins[3])
		{
			s[3]=s[3]+1;
			t4=s[0]+s[1]+s[2]+s[3];
		}
	}
	if(t1>=t2 && t1>=t3 && t1>=t4)
	{
		return p;
	}
	else if(t2>=t1 && t2>=t3 && t2>=t4)
	{
		return q;
	}
	else if(t3>=t1 && t3>=t2 && t3>=t4)
	{
		return r;
	}
	else
		return s;
}
int main()
{
	int i,j;
	int price=12;
	int coins[]={5,3,2,1};
	int value[]={1,5,10,25};
	vector<int> ans=bruteforce(price,coins);
	cout<<ans[0]<<endl;
	cout<<ans[1]<<endl;
	cout<<ans[2]<<endl;
	cout<<ans[3]<<endl;
}