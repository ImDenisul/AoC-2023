def verificare(linii, valori):
    nr=0
    al_catlea=0
    j=0
    hastaguri=[]
    while(j < len(linii)):
        if linii[j] == '#':
            nr+=1
        else:
            if nr != 0:
                hastaguri.append(nr)
                nr=0
        j+=1
    if nr != 0:
        hastaguri.append(nr)

    if hastaguri == valori:
        return True
    else:
        return False


def f(linii, valori):
    if '?' not in linii:
        if verificare(linii, valori):
            global nr_combinatii
            nr_combinatii+=1
            print(linii)
        return 
    j=0
    while j < len(linii):
        if linii[j] == '?':
            linii[j] = '#'
            f(linii, valori)
            linii[j] = '.'
            f(linii, valori)
            linii[j] = '?'
            return
        j+=1




with open('X:\\Proiecte\\alt proiect\\imput.txt', 'r') as fisier:
    linii= fisier.read().splitlines()
    for i in range(len(linii)):
        linii[i] = linii[i].split(' ')
    valori = [x[1].split(',') for x in linii]
    for i in range(len(valori)):
        for j in range(len(valori[i])):
            valori[i][j] = int(valori[i][j])
    linii = [list(x[0]) for x in linii]
    print(linii)
    print(valori)
    nr_combinatii = 0
    for i in range(len(linii)):
        f(linii[i] , valori[i])
    print(nr_combinatii)
       