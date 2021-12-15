import queue
import time
from time import *

#STack and operations
S=[]
S.append('Monday')
S.append('Tuesday')
S.append('Wednesday')
S.append('Thursday')
print(S)
item = S.pop()
print(S)
item = S.pop()
print(S)

#Queue and operations
Q=[]
Q.append('Monday')
Q.append('Tuesday')
Q.append('Wednesday')
Q.append('Thursday')

print(Q)
Q.pop(0)
print(Q)
Q.pop(0)
print(Q)
Q.pop(0)
print(Q)
Q.pop(0)
print(Q)

#Priority queue
PQ = queue.PriorityQueue()
PQ.put((1, 'Monday'))
PQ.put((4, 'Tuesday'))
PQ.put((0.1, 'Wednesday'))

#Tuple
T = (1, 2, 3, 4, 5)
print(T)
print(T[0])
print(T[1:3])

#List vs set
L2 = list(range(10000000))
ST = set(range(10000000))
start = time()
print(9999999 in ST)
end = time()
print(end - start)

#Set operations
S1 = {'Jan', 'Jakub', 'Petra', 'Jana', 'Marketa'}
S2  = {'Jakub', 'Jana', 'Petr'}
S = S1.union(S2)    #Unique names
S = S1.intersection(S2)    #Intersect of names
SC = S2.intersection(S1)    #Intersect of names
SA = S1.difference(S2)    #Unique names
SB = S2.difference(S2)    #Unique names
print(SA)
print(SB)

Sa={(0,0), (1,1), (2,0)}
Sb={(10,10), (0,0)}
S = Sa.union(Sb)  
print(S)

#Dictionary
D = {1357:('Jan', 'Novak', 'Paid'), 4567:('Petra', 'Kolarova', 'No transaction')}
print(1357 in D)
print(D.get(1357))

