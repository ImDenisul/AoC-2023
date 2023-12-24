with open('X:\\Proiecte\\alt proiect\\imput.txt', 'r') as fisier:
    mapa= fisier.read().split('\n')
    k = len(mapa)
    v =[k for _ in range(len(mapa[0]))]
    sum=[0 for _ in range(len(mapa[0]))]
    print(v)
    print(mapa[1])

    for i in range(k):
        for j in range(len(mapa[i])):
            if mapa[i][j]=='#':
                v[j]=k-i-1
            if mapa[i][j]=='O':
                sum[j]+=v[j]
                v[j]-=1

    print(sum)
    Suma=0
    for i in sum:
        Suma+=i
    print(Suma)
        