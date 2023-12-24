# def Cycle():
#         v.sort( key = lambda x: (x[0],x[1]))
        
#         #sus
#         for i in range (len(v)):
#             while(((v[i][0]-1,v[i][1]) not in Hastg and (v[i][0]-1,v[i][1]) not in v) and v[i][0]>0):
#                     v[i]=(v[i][0]-1,v[i][1])
#         v.sort( key = lambda x: (x[1],x[0]))
#         #stanga
#         for i in range (len(v)):
#             while(((v[i][0],v[i][1]-1) not in Hastg and (v[i][0],v[i][1]-1) not in v) and v[i][1]>0):
#                     v[i]=(v[i][0],v[i][1]-1)
#         v.sort( key = lambda x: (x[0],x[1]), reverse = True)
#         #jos
#         for i in range (len(v)):
#             while(((v[i][0]+1,v[i][1]) not in Hastg and (v[i][0]+1,v[i][1]) not in v) and v[i][0]<len(mapa)-1):
#                     v[i]=(v[i][0]+1,v[i][1])
#         v.sort( key = lambda x: (x[1],x[0]), reverse = True )
#         #dreapta
#         for i in range (len(v)):
#             while(((v[i][0],v[i][1]+1) not in Hastg and (v[i][0],v[i][1]+1) not in v) and v[i][1]<len(mapa[0])- 1):
#                     v[i]=(v[i][0],v[i][1]+1)
def Cycle():
    global v
    ####sus####
    v2=[]
    for i in range(len(v)):
        for j in range(len(Dreapta[v[i][1]])):
            if v[i][0]<= Dreapta[v[i][1]][j][0]:
                break
        temp = Dreapta[v[i][1]][j-1][0]+1
        while True:
            if (temp,v[i][1])  in v2:
                temp+=1
            else:
                break   
        v2.append((temp,v[i][1]))
    del v
    v=v2
    del v2
    ####stanga####
    v2=[]
    for i in range(len(v)):
        for j in range(len(Stanga[v[i][0]])):
            if v[i][1]<= Stanga[v[i][0]][j][1]:
                break
        temp = Stanga[v[i][0]][j-1][1]+1
        while True:
            if (v[i][0],temp)  in v2:
                temp+=1
            else:
                break   
        v2.append((v[i][0],temp))
    del v
    v=v2
    del v2
    ####jos####
    v2=[]
    for i in range(len(v)):
        for j in range(len(Dreapta[v[i][1]])):
            if v[i][0]<= Dreapta[v[i][1]][j][0]:
                break
        temp = Dreapta[v[i][1]][j][0]-1
        while True:
            if (temp,v[i][1])  in v2:
                temp-=1
            else:
                break   
        v2.append((temp,v[i][1]))
    del v
    v=v2
    del v2

    ####dreapta####
    v2=[]
    for i in range(len(v)):
        for j in range(len(Stanga[v[i][0]])):
            if v[i][1]<= Stanga[v[i][0]][j][1]:
                break
        temp = Stanga[v[i][0]][j][1]-1
        while True:
            if (v[i][0],temp)  in v2:
                temp-=1
            else:
                break   
        v2.append((v[i][0],temp))
    del v
    v=v2
    del v2


   
    
    

            
        


with open('X:\\Proiecte\\alt proiect\\imput.txt', 'r') as fisier:
    mapa= fisier.read().split('\n')
    k = len(mapa)
    # coordonatele de pe harta
    Stanga=[[(i,-1),(i,len(mapa))] for i in range(len(mapa[0]))]
    Dreapta=[[(-1,i),(len(mapa),i)] for i in range(len(mapa))]

    # Stg = Stanga.copy()
    # Drp = Dreapta.copy()
    v=[]
    Hastg=[]

    def printare(v):
        for i in range(len(mapa)):
            for j in range(len(mapa[i])):
                if (i,j) in v:
                    print('O',end='')
                elif (i,j) in Hastg:
                    print('#',end='')
                else:
                    print('.',end='')
            print()
        print()

    for i in range(k):
        for j in range(len(mapa[i])):
            if mapa[i][j]=='#':
                 Stanga[i].append((i,j))
                 Dreapta[j].append((i,j))
                 Hastg.append((i,j))
            if mapa[i][j]=='O':
                v.append((i,j))
for i in range(len(Stanga)):
    Stanga[i].sort(key = lambda x: x[1])
for i in range(len(Dreapta)):
    Dreapta[i].sort(key = lambda x: x[0])

v.sort( key = lambda x: (x[1],x[0]))
combinatii=[v.copy()]
i=0
print("s-ar putea sa dureze ceva timp")
while True:
    i+=1
    Cycle()
    v.sort( key = lambda x: (x[1],x[0]))
    if v in combinatii:
         break
    combinatii.append(v.copy())
    
v=combinatii[(1000000000 - combinatii.index(v)) % (i - combinatii.index(v)) + combinatii.index(v)]

sum=0
for i in v:
    sum += len(mapa) - i[0]
print("rezultat=",sum)      



