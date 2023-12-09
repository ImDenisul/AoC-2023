
harta ={}
with open('X:\\Proiecte\\alt proiect\\imput.txt', 'r') as fisier:
    pasi = fisier.readline()
    fisier.readline()
    for v in fisier:
         harta[v[0:3:1]] = (v[7:10:1] ,v[12:15:1])
    
    print(harta)
    ok=1
    i=0
    Nrpasi = 0
    curent = 'AAA'
    while(ok):
        Nrpasi+=1
        if(pasi[i]=='R'):
            curent = harta[curent][1]
        else:
            curent = harta[curent][0]
        if(curent == 'ZZZ'):
            ok=0
        if(i < len(pasi)-2):
            i+=1
        else:
            i=0
    print(Nrpasi)