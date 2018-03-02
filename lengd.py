s= input("")
temp1= 0
#counting how many alphabetic ther is
for i in range(len(s)):
    if s[i].isalpha():
        temp1+=1
x = 0
y = 0
# find a word ina string .. word= only alphabetic
for j in range(len(s)):
    if s[j].isalpha():
        if y ==0:
            x+=1
            y+=1
        else:
            continue
    else:
        y = 0
# letter / word        
print(temp1/x)
