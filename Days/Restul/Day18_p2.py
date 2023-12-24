with open('X:\\Proiecte\\alt proiect\\imput.txt', 'r') as fisier:
    pasi = fisier.read().splitlines()
    pasi = [i.split(' ') for i in pasi]
    perimetru = 0
    coordonate = [(0,0)]
    for i in pasi:
        temp = int(i[2][2:-2],16)
        perimetru += temp
        if i[2][-2]=="0":
            coordonate.append((coordonate[-1][0]+temp,coordonate[-1][1]))
        if i[2][-2]=="2":
            coordonate.append((coordonate[-1][0]-temp,coordonate[-1][1]))
        if i[2][-2]=="3":
            coordonate.append((coordonate[-1][0],coordonate[-1][1]+temp))
        if i[2][-2]=="1":
            coordonate.append((coordonate[-1][0],coordonate[-1][1]-temp))
    print(coordonate)
    arie = 0
    for i in range(len(coordonate)-1):
        arie += coordonate[i][0]*coordonate[i+1][1]-coordonate[i+1][0]*coordonate[i][1]
    arie = abs(arie/2)
    print(arie)
    arie += perimetru//2+1
    print("raspuns=",arie)
    print(perimetru)
        

        