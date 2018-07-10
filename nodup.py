import collections
s= input()
s= s.split()
s= collections.Counter(s)
svar=""
for i in s:
    if s[i] > 1:
        svar= "no"
        break
    else:
        svar="yes"
print(svar)
