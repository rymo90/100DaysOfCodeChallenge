from string import ascii_uppercase
s= input()
ms= s[0:len(s)//2]
ms2= s[len(s)//2:]
def DRM(message):
    alphabet=""
    kod=""
    index=0
    jump=0
    for c in ascii_uppercase:
        alphabet+=c
    for i in message:
        index += alphabet.find(i)
    for j in message:
        jump= (alphabet.find(j)+index) % len(alphabet)
        kod+= alphabet[jump]
    return kod
def krypto(dr1,dr2):
    alphabet=""
    kod =""
    dr2num=0
    dr1num=0
    message=""
    for c in ascii_uppercase:
        alphabet+=c
    for i in range(len(dr2)):
        dr2num= alphabet.find(dr2[i])
        dr1num= alphabet.find(dr1[i])
        num = ((dr1num+dr2num)%len(alphabet))
        message += alphabet[num]
    print(message)
dr1= DRM(ms)
dr2= DRM(ms2)
krypto(dr1,dr2)
