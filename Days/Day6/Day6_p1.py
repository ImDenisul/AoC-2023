import re

with open('X:\\Proiecte\\alt proiect\\imput.txt', 'r') as fisier:
    timp = fisier.readline()
    distanta = fisier.readline()
    timp =timp.split()
    distanta= distanta.split()
    del timp[0]
    del distanta[0]
    win=0
    timp = [int(i) for i in timp]
    distanta = [int(i) for i in distanta]
    rezultat = 1
    for i in range(len(timp)):
        for j in range(timp[i]+1):
            if(distanta[i] < j*(timp[i]-j)):
                win+=1
        rezultat *= win
        win = 0
    print(rezultat)

    print(timp)
    print(distanta)