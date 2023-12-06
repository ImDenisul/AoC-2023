import re

with open('X:\\Proiecte\\alt proiect\\imput.txt', 'r') as fisier:
    timp = fisier.readline()
    distanta = fisier.readline()
    timp =timp.split()
    distanta= distanta.split()
    timp = [''.join(timp)]
    distanta = [''.join(distanta)]
    timp= re.split('[:]', timp[0])
    distanta= re.split('[:]', distanta[0])
    del timp[0]
    del distanta[0]
    timp = int(timp[0])
    distanta = int(distanta[0])
    print(timp)
    rezultat = 1
    win=0
    for j in range(timp+1):
        if(distanta < j*(timp-j)):
            intermalStg = j
            break

    for j in range(timp+1,-1,-1):
        if(distanta < j*(timp-j)):
            intermalDr = j
            break
    rezultat = intermalDr - intermalStg+1
    print(rezultat)
