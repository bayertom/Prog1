a=3
b=-7
c=-1

#Var1
#A is smallest
if (a<b) and (a<c):
    m = a
if (b<a) and (b<c):
    m = b
if (c<a) and (c<b):
    m = c
print(m)

#Var2
#A is smallest
if (a<b) and (a<c):
    m = a
elif b < c:
    m = b
else:
    m = c

#Var3
if (a<b):
    m = a
else:
    m = b
if c < m:
    m = c

print(m)