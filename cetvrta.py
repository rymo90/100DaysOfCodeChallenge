sx= set()
sy= set()
for i in range(3):
    p= [int(i) for i in input().split()]
    if p[0] in sx:
        sx.remove(p[0])
    else:
        sx.add(p[0])
    if p[1] in sy:
        sy.remove(p[1])
    else:
        sy.add(p[1])
print(sx.pop(),sy.pop())
