unsortedList = [["redwan",7],["hashim",9], ["amal",6], ["kemer", 1], ["yassin", 5], ["anwar", 0], ["jemal",4]]
max =0
sortedList = [["", 0]] *(len(unsortedList)+1) # make a copy of original list
for i in range(len(unsortedList)):    # find max value in original list.
    if max < unsortedList[i][1]:
        max = unsortedList[i][1]
        
def d_c(unsortedList, max,sortedList): 
    count = [0] *( max +1 ) # initiolize an array with with length of max and set it to  zero.
    temp= 0
    for j in range(len(unsortedList)): # set plus one for every accurent in original list .. 
        count[unsortedList[j][1]] += 1  # = in count array with correspanding index.
    for i in range(len(count)): # add previous value with current value in count.
        count[i] += temp 
        temp = count[i]   
    for i in range(len(unsortedList)-1,-1, -1): # satrt from last to first in original list
        originalValue = unsortedList[i][1]       # take the key and valuefrom original and sett value  in index acount
        originalKey = unsortedList[i][0]         
        returnContIdex = count[originalValue]   # take the value of count and  set in sort list index. 
        count[originalValue] -= 1               # set -1 after you return vaue of count
        sortedList[returnContIdex] = [originalKey, originalValue ] # set the return valu of cunt and set it in index of sorted list
        # and give key and value from original list
d_c(unsortedList,max, sortedList)
