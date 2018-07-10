n= int(input())
svar=""
for i in range(n):
    c= input()
    c= c.split()
    product= int(c[len(c)-1])
    c = c[0:len(c)-1]
    c.sort(reverse = True, key= int)
    # print(c)
    if (int(c[0]) + int(c[1])) == product:
        svar="Possible"
    elif (int(c[0]) / int(c[1])) == product:
        svar="Possible"
    elif (int(c[0]) - int(c[1])) == product:
        svar="Possible"

    elif (int(c[0]) * int(c[1])) == product:
        svar="Possible"
    else:
        svar="Impossible"
    print(svar)
