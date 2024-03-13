import random as rd

N = 1000

egg11 = 0
egg22 = 0
ingen = 0 

for i in range(N):
    egg1 = rd.randint(0,12)
    egg2 = rd.randint(0,12)
    
    if egg1 == 1:
        egg11 = egg11 +1
        
        
    elif egg1 == 1 and egg2 ==2:
        egg22 = egg22 +1
       
    
    else:
        ingen = ingen +1

ettegg = egg11/N
toegg = egg22/N
ingenegg = ingen/N

print(f"sannsyneligheten for 1 egg er {ettegg}")

print(f"sannsyneligheten for 2 egg er {toegg}")

print(f"sannsyneligheten for ingen egg er {ingenegg}")

print(f"sum = {ingenegg + ettegg + toegg}")
       
    