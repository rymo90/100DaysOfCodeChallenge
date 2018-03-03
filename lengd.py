s= input("")
countLetter= 0
word = 0
notWord = 0
# find a word ina string .. word= only alphabetic
for j in range(len(s)):
    if s[j].isalpha():
        countLetter +=1
        if notWord ==0:
            word+=1
            notWord+=1
        else:
            continue
    else:
        notWord = 0
# letter / word        
print(countLetter/word)
