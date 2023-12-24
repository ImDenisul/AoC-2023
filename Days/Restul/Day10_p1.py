def cautare_tava(i,j,I,J,Nr):
    for k in tevi:
            if k == harta[I][J]:
                if (I + tevi[k][0][0] == i and J + tevi[k][0][1] == j):
                    
                    return ( I + tevi[k][1][0], J + tevi[k][1][1])
                if (I + tevi[k][1][0] == i and J + tevi[k][1][1] == j):
                    
                    return ( I + tevi[k][0][0], J + tevi[k][0][1])
    return 0



tevi ={'|':[(-1,0),(1,0)],'-':[(0,1),(0,-1)],'L':[(-1,0),(0,1)],'J':[(-1,0),(0,-1)],'7':[(1,0),(0,-1)],'F':[(1,0),(0,1)]}
with open('X:\\Proiecte\\alt proiect\\imput.txt', 'r') as fisier:
    harta = fisier.read()
    harta = harta.split('\n')
    harta = [list(x) for x in harta]
    ok=0
    for i in range(len(harta)):
        if(ok):
            i-=1
            break
        
        for j in range(len(harta[0])):
            if(harta[i][j] == 'S'):
                harta[i][j] = 0
                ok=1
                break
    print('start=',i,j)
    Nr = 1

    # I=0
    # J=0
    # I =cautare_tava(i,j,0,-1,Nr)
    # if(I==0):
    #     I =cautare_tava(i,j,0,1,Nr)
    #     if(I==0):
    #         I =cautare_tava(i,j,-1,0,Nr)
    #     else:
    #         J=cautare_tava(i,j,-1,0,Nr)
    # else:
    #     J=cautare_tava(i,j,1,0,Nr)

    
    # print(cautare_tava(i,j,i+1,j,Nr))
    ok=1
    if(cautare_tava(i,j,i+1,j,Nr)!=0):
        coordonate =(i+1,j)
    elif(cautare_tava(i,j,i-1,j,Nr)!=0):
        coordonate =(i-1,j)
    elif(cautare_tava(i,j,i,j+1,Nr)!=0):
        coordonate =(i,j+1)
    elif(cautare_tava(i,j,i,j-1,Nr)!=0):
        coordonate =(i,j-1)
    
    while(ok):
        if(harta[coordonate[0]][coordonate[1]] == 0):
            break
        temp = coordonate
        coordonate = cautare_tava(i,j,coordonate[0],coordonate[1],Nr)
        i=temp[0]
        j=temp[1]
        Nr+=1

    print(Nr//2)