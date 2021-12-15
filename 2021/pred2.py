#Prevod DMS
alpha_deg = 10
alpha_min = 20
alpha_sec = 30
alpha = alpha_deg + alpha_min/60 + alpha_sec / 3600
print(alpha)

#Zpetny prevod
deg = int(alpha)
print(deg)
min_float = (alpha - deg)*60
print(min_float)
min = int(min_float)
print(min)
sec = (min_float - min)*60
print(sec)

#Jednoducha prace s listem
L = []
L2 = [1, 2, 3 ,4]
print(L2)
L2.append(5)
print(L2)
print(L2[2])
print(L2[:])
L2.pop(0)
print(L2)
