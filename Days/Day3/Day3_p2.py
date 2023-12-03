def formare_numar(linie , k):
    v=[]
    info = [0,0]
    i=k+1
    while(i+1<len(linie) and linie[i].isdigit() ):
        v.append(linie[i])
        i+=1
    i=k
    while(i>=0 and linie[i].isdigit()):
        v.insert(0,linie[i])
        i-=1
    info[0]=i+1
    info[1]=0
    k=1
    for j in v[::-1]:
        info[1]+=int(j)*k
        k*=10
    return info    

caractere ="*"

coordonate ={}

sum=0
with open('X:\\Proiecte\\alt proiect\\imput.txt', 'r') as fisier:
    linie_sus = fisier.readline()
    Nr_linie = 0
    for linie in fisier:
        linie_jos = linie
        i=0
        while(i<len(linie_sus)):
            if(linie_sus[i]!='.' and linie_sus[i] in caractere):
                if (i-1>0 and linie_sus[i-1].isdigit()):
                    info = formare_numar(linie_sus,i-1)
                    cor = (Nr_linie,i)
                    if(cor in coordonate):
                        coordonate[cor].append(info[1])
                    else:
                        coordonate[cor]=[info[1]]
                    linie_sus= linie_sus[:info[0]] + "." * len(str(info[1])) + linie_sus[len(str(info[1]))+info[0]:]

                
                if (i+1<len(linie_sus) and linie_sus[i+1].isdigit()):
                    info = formare_numar(linie_sus,i+1)
                    cor = (Nr_linie,i)
                    if(cor in coordonate):
                        coordonate[cor].append(info[1])
                    else:
                        coordonate[cor]=[info[1]]
                    linie_sus= linie_sus[:info[0]] + "." * len(str(info[1])) + linie_sus[len(str(info[1]))+info[0]:]
                if (i-1>0 and i <len(linie_jos) and linie_jos[i-1].isdigit()):
                    info = formare_numar(linie_jos,i-1)
                    cor = (Nr_linie,i)
                    if(cor in coordonate):
                        coordonate[cor].append(info[1])
                    else:
                        coordonate[cor]=[info[1]]
                    linie_jos= linie_jos[:info[0]] + "." * len(str(info[1])) + linie_jos[len(str(info[1]))+info[0]:]
                if (i <len(linie_jos) and linie_jos[i].isdigit()):
                    info = formare_numar(linie_jos,i)
                    cor = (Nr_linie,i)
                    if(cor in coordonate):
                        coordonate[cor].append(info[1])
                    else:
                        coordonate[cor]=[info[1]]
                    linie_jos= linie_jos[:info[0]] + "." * len(str(info[1])) + linie_jos[len(str(info[1]))+info[0]:]
                if (i <len(linie_jos) and linie_jos[i+1].isdigit()):
                    info = formare_numar(linie_jos,i+1)
                    cor = (Nr_linie,i)
                    if(cor in coordonate):
                        coordonate[cor].append(info[1])
                    else:
                        coordonate[cor]=[info[1]]
                    linie_jos= linie_jos[:info[0]] + "." * len(str(info[1])) + linie_jos[len(str(info[1]))+info[0]:]
            if(linie_sus[i].isdigit()):
                if (i-1>0 and i <len(linie_jos) and linie_jos[i-1]!='.' and  linie_jos[i-1] in caractere):
                    info = formare_numar(linie_sus,i)
                    cor = (Nr_linie+1,i-1)
                    if(cor in coordonate):
                        coordonate[cor].append(info[1])
                    else:
                        coordonate[cor]=[info[1]]
                    linie_sus= linie_sus[:info[0]] + "." * len(str(info[1])) + linie_sus[len(str(info[1]))+info[0]:]
                if (i-1>0 and i <len(linie_jos) and linie_jos[i]!='.' and  linie_jos[i] in caractere):
                    info = formare_numar(linie_sus,i)
                    cor = (Nr_linie+1,i)
                    if(cor in coordonate):
                        coordonate[cor].append(info[1])
                    else:
                        coordonate[cor]=[info[1]]
                    linie_sus= linie_sus[:info[0]] + "." * len(str(info[1])) + linie_sus[len(str(info[1]))+info[0]:]
                if (i <len(linie_jos) and linie_jos[i+1]!='.' and  linie_jos[i+1] in caractere):
                    info = formare_numar(linie_sus,i)
                    cor = (Nr_linie+1,i+1)
                    if(cor in coordonate):
                        coordonate[cor].append(info[1])
                    else:
                        coordonate[cor]=[info[1]]
                    linie_sus= linie_sus[:info[0]] + "." * len(str(info[1])) + linie_sus[len(str(info[1]))+info[0]:]
            i+=1
        linie_sus = linie_jos
        Nr_linie+=1
    
    for i in range(len(linie_sus)):
        if(linie_sus[i]!='.'and linie_sus[i] in caractere):
                if (i+1<len(linie_sus) and linie_sus[i+1].isdigit()):
                    info = formare_numar(linie_sus,i)
                    cor = (Nr_linie,i+1)
                    if(cor in coordonate):
                        coordonate[cor].append(info[1])
                    else:
                        coordonate[cor]=[info[1]]
                if (i-1>0 and linie_sus[i-1].isdigit()):
                    info = formare_numar(linie_sus,i)
                    cor = (Nr_linie,i-1)
                    if(cor in coordonate):
                        coordonate[cor].append(info[1])
                    else:
                        coordonate[cor]=[info[1]]

for valori in coordonate.values():
    if(len(valori)==2):
        sum+=valori[0]*valori[1]

print("sum=",sum)