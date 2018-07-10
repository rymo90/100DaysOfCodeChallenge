import collections
n= int(input())
for line in range(n):
    g= input()
    tmp= input()
    tmp = tmp.split()
    c= collections.Counter(tmp)
    for i in c:
        if c[i]==1:
            print("Case #"+str(line+1)+":"+" "+i)
