import sys 
class ArrayQ:# föreläsning 2

    def __init__(self):  # en tom lista
        self._lista =[]

    def enqueue (self, nummer):         #  en motod som lägger till i lista
        return self._lista.append(nummer)

    def dequeue (self):    # tar bor och returnera värden
        return self._lista.pop(0)

    def isEmpty (self):          # kollar om lista är tom
        return self._lista == []
    def peek(self):
        return self._lista[len(self._lista)-1]      
q = ArrayQ()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.enqueue(6)
q.enqueue(7)
q.enqueue(8)
q.enqueue(9)
q.enqueue(10)
q.enqueue(11)
q.enqueue(12)
resa = []
x = 0
while not q.isEmpty():
    if x == 0:
        tarbort = q.dequeue()
        x=1
        resa.append(tarbort)
    else:
        y = q.dequeue()
        q.enqueue(y)    
        x= 0   
print(resa)        



#