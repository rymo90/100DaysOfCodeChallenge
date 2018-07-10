s = input()
svar="no hiss"
for i in range(len(s)-1):
    if s[i]== 's' and s[i+1]== 's':
        svar= "hiss"
        break
    else:
        svar= "no hiss"
print(svar)
