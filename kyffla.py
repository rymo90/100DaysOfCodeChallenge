import sys
class ArrayQ:# föreläsning 2

    def __init__(self):  # en tom lista
        self._lista =[]

    def enqueue (self, nummer):         #  en motod som lägger till i lista
        return self._lista.append(nummer)

    def dequeue (self):    # tar bor och returnera värden
        return self._lista.pop(0)

    def isEmpty (self):          # kollar om lista är tom
        if self._lista == []:
            return True
        else:
            return False
    def peek(self):
        return self._lista[len(self._lista)-1]
    def size(self):
        return len(self._lista)
q = ArrayQ()
q.enqueue("1")
q.enqueue("2")
q.enqueue("3")
q.enqueue("4")
q.enqueue("5")
q.enqueue("6")
q.enqueue("7")
q.enqueue("8")
q.enqueue("9")
q.enqueue("10")
q.enqueue("11")
q.enqueue("12")

# q.enqueue("kasta")
# q.enqueue("ord")
# q.enqueue("om")
#
# q.enqueue("3.4")
# q.enqueue("2.3")
# q.enqueue("5")
# q.enqueue("185")
# q.enqueue("23")

def oddKyffla(q,s,x,y):
    while not q.isEmpty() and q.size() >y:
        if x == 0:
            tarbort = q.dequeue()
            s.append(tarbort)
            x=1
            y +=1
        else:
            tarbort = q.dequeue()
            q.enqueue(tarbort)
            x= 0
    while not q.isEmpty():
        oddKyffla(q,s,0,0)
    return s
def evenKyffla(q,s,x):
    while not q.isEmpty():
        if x == 0:
            tarbort = q.dequeue()
            s.append(tarbort)
            x=1
        else:
            tarbort = q.dequeue()
            q.enqueue(tarbort)
            x= 0
    return s
x = 0
y = 0
result = []

if q.size()%2==0:
    kyffla = evenKyffla(q,result,x)
else:
    kyffla = oddKyffla(q,result,x,y)
print(kyffla)
#
