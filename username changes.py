t=int(input())
for i in range(t):
    name=input()
    l=len(name)
    n = ord(name[0])
    flag = 0
    for j in range(1,l):
        n1=ord(name[j])

        if(n1<n):
            flag=flag+1
        else:
            pass
    if(flag>0):
        print("YES")
    else:
        print("NO")
