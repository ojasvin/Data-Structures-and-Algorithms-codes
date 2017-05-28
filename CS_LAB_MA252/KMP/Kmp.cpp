#include <iostream>
#include <string>
using namespace std;

int main()
{
    string p,t;
    cout<<"Enter the pattern::"<<endl;
    cout<<"Enter the string::"<<endl;	
    cin>>p;    	
    cin>>t;
    long int n,c;	  
    n=p.length();	
    long int pi[n],i,j;
    i=1;
    j=0;
    pi[0]=0;
    while(i<n)
    {
        if (p[i]!=p[j])
        {
            if (j==0)
            {
                pi[i]=0;
                i=i+1;
                
            }    
            else
            {
                j=p[j];
                
            }
        }
        else
        {
            pi[i]=j+1;
            i=i+1;
            j=j+1;
        }    
    }
    //for (i=0;i<n;i++)
    //cout<<pi[i]<<endl;//code is ok
    
    j=0;
    i=0;
    c=0;
    while (j<t.length())
    {
        if (p[i]==t[j])
        {
            if (i==n-1)    
                c++;   
            i++;
            j++;
        }
        else
        {
            if (i==0)
                j++;
            else
                i=pi[i-1];
        }    
        
             
    }    
    cout<<"The number of occurences of pattern in string is:::"<<endl;
    cout<<c;
    return 0;	
}    
      
        
        
