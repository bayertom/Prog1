#Immutable object
def f(x):
    x = 7
    print(id(x))

#Mutable object
def f2(L):
    L[0] = 7
    print(id(L))

#ICompute distance
def dist(x1=0, y1=0, x2=0, y2=0):
    dx = x2 - x1
    dy = y2 - y1
    d = (dx*dx + dy*dy)**0.5
    return d

#Non-keyword arguments
def sum (*X):
    s=0
    for x in X:
        s+=x
    return s

#Keyword arguments
def dictPrint(**X):
    for x in X:
        print(x, X[x])


#Recursive function
def fr(n, s):
    s += '   '
    print(s+"C(" + str(n)+")")        
    if (n == 1):
        print(s+"D");                   
    else:
        print(s+"f(" + str(n-1) + ")")
        fr(n - 1, s)                    
    print(s+"E(" + str(n) + ")")      

#Immutable
a = 10
print(id(a))
f(a)
print(a)

#Mutable
L=[1, 2, 3]
print(id(L))
f2(L)
print(L)

#Distance
print(dist())
print(dist(1,1,-1, -1))

#Keyword/non-keyword arguments
print(sum(1, 2, 3, 4, 5, 6))
print(dictPrint(name='Jana', sur='Novak', age='21'))

#Recursiv function
fr(5,'')