
def f(n):
    #Factorial
    if n > 1:
        return n * f(n-1)
    else:
        return 1

def fib(n):
    #Fibonacci
    if n > 1:
        return fib(n-1) + fib(n-2)
    else:
        return 1

def maximum(x, l, r):
    #Find maximum
    if r - l > 1:
        m = (l + r) //2
        lmax = maximum(x, l, m)
        rmax = maximum(x, m, r)
        return max(lmax, rmax)
    else:
        return max(x[l], x[r])


#Factorial
fact = f(4)
print(fact)

#Fibonacci
#print(fib(40))

#Find maximum
X = [5, 6, 13, -8, 19]
print(maximum(X, 0, len(X)-1))