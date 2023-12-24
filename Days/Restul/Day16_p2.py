
def parcurgere(D,i,j):
    h=0
    while(i>=0 and i<len(harta) and j>=0 and j<len(harta[0])):
        global Nrene
            
        if harta[i][j] in oglinzi:
            for k in range(len(oglinzi[harta[i][j]])):
                if D == oglinzi[harta[i][j]][k][0]:
                    if len(oglinzi[harta[i][j]][k])==2:
                        D = oglinzi[harta[i][j]][k][1]
                    if len(oglinzi[harta[i][j]][k])>2:
                        if energized[i][j]=='.':
                            energized[i][j]='X'
                            Nrene +=1
                            parcurgere(oglinzi[harta[i][j]][k][2],i+directii[oglinzi[harta[i][j]][k][2]][0],j+directii[oglinzi[harta[i][j]][k][2]][1])
                            parcurgere(oglinzi[harta[i][j]][k][1],i+directii[oglinzi[harta[i][j]][k][1]][0],j+directii[oglinzi[harta[i][j]][k][1]][1])
                            return
                        else:
                            return
                    break
        if energized[i][j]=='.':
            energized[i][j]='X'
            Nrene +=1
            
        i+=directii[D][0]
        j+=directii[D][1]
    return 




directii = {'^':(-1,0), 'v':(1, 0), '<':(0, -1), '>':(0,1)}
oglinzi = {'/':[('^','>'), ('v', '<'), ('<', 'v'), ('>' , '^')], '\\':[('^', '<'), ('v', '>'), ('<', '^'), ('>' , 'v')],
           '|':[('^', '^'), ('v', 'v'),('>','^','v'),('<','^','v')], '-':[('<', '<'), ('>', '>'), ('^','<','>'),('v','<','>')]}


with open('X:\\Proiecte\\alt proiect\\imput.txt', 'r') as fisier:
    harta = fisier.read().split('\n')
    energized =[['.'for i in range(len(harta[0]))] for j in range(len(harta))]
    energizedcopy =[['.'for i in range(len(harta[0]))] for j in range(len(harta))]
    Nrene =0
    # parcurgere('v',0,3)
    # print(Nrene)
    NRX=0
    max = 0
    for i in range(len(harta)):
        Nrene =0
        parcurgere('>',i,0)
        print(Nrene)
        if Nrene>max:
            max = Nrene
        del energized
        energized=[['.'for i in range(len(harta[0]))] for j in range(len(harta))]

        Nrene =0
        parcurgere('<',i,len(harta[0])-1)
        print(Nrene)
        if Nrene>max:
            max = Nrene
        del energized
        energized=[['.'for i in range(len(harta[0]))] for j in range(len(harta))]

    for i in range(len(harta[0])):
        Nrene =0
        parcurgere('v',0,i)
        print(Nrene)
        if Nrene>max:
            max = Nrene
        del energized
        energized=[['.'for i in range(len(harta[0]))] for j in range(len(harta))]

        Nrene =0
        print(Nrene)
        parcurgere('^',len(harta)-1,i)
        if Nrene>max:
            max = Nrene
        del energized
        energized=[['.'for i in range(len(harta[0]))] for j in range(len(harta))]
    print(max)

    