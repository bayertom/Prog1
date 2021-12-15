#Faktorial
n = 6
f = 1
while n > 1:
    f *= n
    n -= 1

print(f)

#Maximum
X=[1, 27, 105.5, -7, 94]
x_max = X[0]
for x in X:
    if x > x_max:
        x_max = x

print(type(x_max))

R = range(20)
for r in R:
    print(r)
 
#Maximum 2
X=[1, 27, 105.5, -7, 94]
x_max = X[0]
i_max = 0
for i in range(len(X)):
    if X[i] > x_max:
        x_max = X[i]
        i_max = i

def maximum(X):
    x_max = X[0]
    i_max = 0
    for i in range(len(X)):
        if X[i] > x_max:
            x_max = X[i]
            i_max = i

    return x_max, i_max

v1, v2  = maximum(X)
print(v1, v2)