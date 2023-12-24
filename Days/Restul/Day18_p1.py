with open('X:\\Proiecte\\alt proiect\\imput.txt', 'r') as fisier:
    pasi = fisier.read().splitlines()
    pasi = [i.split(' ') for i in pasi]
    perimetru = 0
    coordonate = [(0,0)]
    for i in pasi:
        perimetru += int(i[1])
        if i[0]=='R':
            coordonate.append((coordonate[-1][0]+int(i[1]),coordonate[-1][1]))
        if i[0]=='L':
            coordonate.append((coordonate[-1][0]-int(i[1]),coordonate[-1][1]))
        if i[0]=='U':
            coordonate.append((coordonate[-1][0],coordonate[-1][1]+int(i[1])))
        if i[0]=='D':
            coordonate.append((coordonate[-1][0],coordonate[-1][1]-int(i[1])))
    print(coordonate)
    arie = 0
    for i in range(len(coordonate)-1):
        arie += coordonate[i][0]*coordonate[i+1][1]-coordonate[i+1][0]*coordonate[i][1]
    arie = abs(arie/2)
    print(arie)
    arie += perimetru//2+1
    print("raspuns=",arie)
    print(perimetru)
        

        