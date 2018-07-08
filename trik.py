import sys
ball= 1
for line in sys.stdin:
    i = line.strip()
for k in range(len(i)):
    if i[k]=='A' :
        if ball ==1:
            ball=2
        elif ball == 2:
            ball= 1
        else:
            continue
    elif i[k]== 'B':
        if ball== 2:
            ball =3
        elif ball == 3:
            ball= 2
        else:
            continue
    else:
        if ball== 3:
            ball=1
        elif ball== 1:
            ball=3
        else:
            continue
print(ball)
