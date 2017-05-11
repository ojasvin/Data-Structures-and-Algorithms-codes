def Pallindrome(s):
    results=set()
    c=0
    for i in s:
        if i not in results:
            results.add(i)
            c=c+1 
    l=len(s)
    for idx in range(0,l):
    #For odd length    
        start,end=idx-1,idx+1
        while start>=0 and end<l and s[start]==s[end]:
            results.add(s[start:end+1])
            c=c+1
            start=start-1
            end=end+1
        
    #For even length
        start,end=idx,idx+1
        while start>=0 and end<l and s[start]==s[end]:
            results.add(s[start:end+1])
            c=c+1
            start=start-1
            end=end+1
            
    return c,results
            
        
s=input()
cd,resultss=Pallindrome(s)
print(cd)
print(resultss)