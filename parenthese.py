def check(val):
    count = 0
    for i in val:
        if i == '(':
            count += 1
        elif i == ')':
            count-=1
        else:
            raise AttributeError("invalid character")
    if count%2==0:
        svar= "Balanserad"
    else:
        svar= "Obalanserad"
    return svar
answer=check("(k)")
print(answer)
