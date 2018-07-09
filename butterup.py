import sys
temp =""
for i in sys.stdin:
    temp += i
lista= temp.split()
sum = 0
dominater= int(lista[0])
for i in range(len(lista)-1):
    if int(lista[i+1]) !=-1:
        sum += int(lista[i+1])
    else:
        dominater -= 1
print(sum/dominater)
