s= input()
count = 0
per= "PER"
sp= list(map(''.join,zip(*[iter(s)]*3)))
for i in range(len(sp)):
    gr= sp[i]
    for j in range(len(gr)):
        if gr[j] != per[j]:
            count+=1
print(count)
