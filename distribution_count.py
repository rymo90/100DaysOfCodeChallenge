import copy
a = [["redwan",7],["hashim",9], ["amal",6], ["kemer", 4], ["yassin", 5], ["anwar", 0], ["jemal",4]]
max = 0
b= copy.copy(a)
for value in range(len(a)):

    if max < a[value][1]:
        max = a[value][1]
for j in range(len(b)):
    b[j][0] = ""
    b[j][1]= 0  
def d_c(a, max,b):
    print("original list", a)
    print("non original list", b)
    count = [0] *( max +1 )
    temp= 0
    for i in range(len(count)):
        count[i] += temp
        temp = count[i]   
    print("counter after", count)    
    # print("loop value")
    for i in range(len(a)-1,0, -1):
        return_A_value = a[i][1]
        # print(return_A_value)
        return_count_value = count[return_A_value]
        count[return_A_value]-=1
        print(return_count_value)
        b[return_count_value][1] = return_A_value
    print(b)   
d_c(a,max, b)