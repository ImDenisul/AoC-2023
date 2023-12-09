import re

def precedentul_pas(istoric):
    ok=1
    diferente =[]
    for i in range(1,len(istoric)):
        diff = istoric[i] - istoric[i-1]
        if diff != 0:
            ok = 0
        diferente.append(diff)
    if ok == 0:
        diferente.insert(0,precedentul_pas(diferente))
    return istoric[0]-diferente[0] 


with open('X:\\Proiecte\\alt proiect\\imput.txt', 'r') as fisier:
    istoric = []
    sum=0
    for pasi in fisier:
        del istoric
        istoric= []
        pasi = pasi.split()
        for i in pasi:
            istoric.append(int(i))
        sum+= precedentul_pas(istoric)

print(sum)
    
