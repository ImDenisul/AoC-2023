imagine = []
coordonate = []
with open('X:\\Proiecte\\alt proiect\\imput.txt', 'r') as fisier:
    imagine = fisier.read().splitlines()
    imagine = [list(x) for x in imagine]
    # i=0
   
    
    i=0
    while i < len(imagine[0]):
        ok=1
        j=0
        while j < len(imagine):
            if imagine[j][i] == '#':
                ok=0
            j+=1
        for k in range(len(imagine)):
            if ok==1:
                imagine[k][i]=-1
        i+=1

    i=0
    while i < len(imagine):
        if '#' not  in imagine[i]:
            imagine[i]= [-1]*len(imagine[i])
        i += 1


scala = 1000000



distantaI = 0
for i in range(len(imagine)):
    distantaJ = 0

    if imagine[i] == [-1]*len(imagine[i]):
        distantaI += scala-1
    
    for j in range(len(imagine[i])):
        if imagine[i][j] == -1:
            distantaJ += scala-1
        if imagine[i][j] == '#':
            coordonate.append([i+distantaI,j+distantaJ])
              



sum= 0
for i in range(len(coordonate)):
    for j in range(i,len(coordonate)):
        sum += abs(coordonate[i][0]-coordonate[j][0]) + abs(coordonate[i][1]-coordonate[j][1])
                
print(imagine)
print(coordonate)
print(sum)
