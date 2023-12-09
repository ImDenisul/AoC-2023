
harta ={}
curent =[]
with open('X:\\Proiecte\\alt proiect\\imput.txt', 'r') as fisier:
    pasi = fisier.readline()
    fisier.readline()
    for v in fisier:
         harta[v[0:3:1]] = (v[7:10:1] ,v[12:15:1])
         if v[2] == 'A':
                curent.append(v[0:3:1])
    pasi_necesari =[]         
    for j in curent:
        ok=1
        i=0
        Nrpasi_to_final = 0
        while(ok):
            Nrpasi_to_final+=1
            if(pasi[i]=='R'):
                j = harta[j][1]
            else:
                j = harta[j][0]
            if(j[-1] == 'Z'):
                ok=0
            if(i < len(pasi)-2):
                i+=1
            else:
                i=0
        Nrpasi_iar_final = 0
        ok=1
        while(ok):
            Nrpasi_iar_final+=1
            if(pasi[i]=='R'):
                j = harta[j][1]
            else:
                j = harta[j][0]
            if(j[-1] == 'Z'):
                ok=0
            if(i < len(pasi)-2):
                i+=1
            else:
                i=0
        pasi_necesari.append((Nrpasi_to_final,Nrpasi_iar_final))
    # i=0
    # k = pasi_necesari[3][0] + pasi_necesari[3][1]*3
    # j= curent[3]
    # while(k):
    #         k-=1
    #         if(pasi[i]=='R'):
    #             j = harta[j][1]
    #         else:
    #             j = harta[j][0]
    #         if(j[-1] == 'Z'):
    #             ok=0
    #         if(i < len(pasi)-2):
    #             i+=1
    #         else:
    #             i=0
    # print(j)

    def dute(harta , start , pasi, NRpasi):
        i=0
        while(NRpasi):
            if(pasi[i]=='R'):
                start = harta[start][1]
            else:
                start = harta[start][0]
            if(i < len(pasi)-2):
                i+=1
            else:
                i=0
            NRpasi-=1
        return start
    
    def cmmdc(a, b):
        while b:
            a, b = b, a % b
        return a

    def cmmmc(a, b):
        return (a * b) // cmmdc(a, b)
    
    Nrpasi = cmmmc(pasi_necesari[0][0],pasi_necesari[1][0])
    for i in range(2,len(pasi_necesari)):
        Nrpasi = cmmmc(Nrpasi,pasi_necesari[i][0])
    print(pasi_necesari)  
    print(Nrpasi)
    print("merge deoarece distanta de la inceput la finale este egala cu distanta de la final la final")
    
        




    # mare = max(pasi_necesari, key=lambda x: x[1])
    # print(mare)
    # ok=1
    # Nrpasi =mare[0]
    # pas = mare[1]
    # while(ok):
    #
    #     ok=0
    #     Nrpasi+=pas
    #     i=0
    #     while(i < len(pasi_necesari)):
    #         if (Nrpasi - pasi_necesari[i][0])%pasi_necesari[i][1] == 0:
    #             print(dute(harta , curent[i] , pasi , Nrpasi))
    #             print(Nrpasi)
    #             pas *= pasi_necesari[i][1]
    #             print(dute(harta , curent[i] , pasi , Nrpasi))
    #             del pasi_necesari[i]
    #         i+=1
    #     if (len(pasi_necesari) != 0):
    #         ok=1
    
  
        
    