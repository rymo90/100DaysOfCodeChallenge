n = int(input())
lis= []
dic= {}
k= 0
for i in range(n):
    t = input()
    t= t.split()
    dic[t[0]] = 0
    lis.append(t)
for j in range(len(lis)):
    if dic[lis[j][0]]==0 and k < 12:
        dic[lis[j][0]]= 1
        k+=1
        print(*lis[j])
