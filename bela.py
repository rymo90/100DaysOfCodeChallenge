sum =  0
value = {"domOrNotDom":{"A": 11, "K": 4, "Q": 3, "T":10,"res":0},"dom":{"J":20,"9": 14},"notDom":{"J":2 ,"9":0}}
h, b = [k for k in input().split()]
for i in range(int(h)):
    j= 0
    while j < 4:
        d = input()
        n = d[0]
        s = d[1]
        if n =="J" or n == "9":
            if b == s:
                sum+= value["dom"][n]
            else:
                sum +=value["notDom"][n]
        else:
            if n == "8" or n =="7":
                sum += value["domOrNotDom"]["res"]
            else:
                sum += value["domOrNotDom"][n]
        j+=1
print(sum)
