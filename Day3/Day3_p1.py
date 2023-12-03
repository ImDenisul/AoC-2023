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
    print(info[1])
    return info    

caractere ="!\"#$%&'()*+,-/:;<=>?@[\]^_`{|}~"

sum=0
with open('X:\\Proiecte\\alt proiect\\imput.txt', 'r') as fisier:
    linie_sus = fisier.readline()
    for linie in fisier:
        linie_jos = linie
        i=0
        while(i<len(linie_sus)):
            if(linie_sus[i]!='.' and linie_sus[i] in caractere):
                if (i-1>0 and linie_sus[i-1].isdigit()):
                    info = formare_numar(linie_sus,i-1)
                    sum+=info[1]
                    linie_sus= linie_sus[:info[0]] + "0" * len(str(info[1])) + linie_sus[len(str(info[1]))+info[0]:]
                
                if (i+1<len(linie_sus) and linie_sus[i+1].isdigit()):
                    info = formare_numar(linie_sus,i+1)
                    sum+=info[1]
                    linie_sus= linie_sus[:info[0]] + "0" * len(str(info[1])) + linie_sus[len(str(info[1]))+info[0]:]
                if (i-1>0 and i <len(linie_jos) and linie_jos[i-1].isdigit()):
                    info = formare_numar(linie_jos,i-1)
                    sum+=info[1]
                    linie_jos= linie_jos[:info[0]] + "0" * len(str(info[1])) + linie_jos[len(str(info[1]))+info[0]:]
                if (i <len(linie_jos) and linie_jos[i].isdigit()):
                    info = formare_numar(linie_jos,i)
                    sum+=info[1]
                    linie_jos= linie_jos[:info[0]] + "0" * len(str(info[1])) + linie_jos[len(str(info[1]))+info[0]:]
                if (i <len(linie_jos) and linie_jos[i+1].isdigit()):
                    info = formare_numar(linie_jos,i+1)
                    sum+=info[1]
                    linie_jos= linie_jos[:info[0]] + "0" * len(str(info[1])) + linie_jos[len(str(info[1]))+info[0]:]
            if(linie_sus[i].isdigit()):
                if (i-1>0 and i <len(linie_jos) and linie_jos[i-1]!='.' and  linie_jos[i-1] in caractere):
                    info = formare_numar(linie_sus,i)
                    sum+=info[1]
                    linie_sus= linie_sus[:info[0]] + "0" * len(str(info[1])) + linie_sus[len(str(info[1]))+info[0]:]
                if (i-1>0 and i <len(linie_jos) and linie_jos[i]!='.' and  linie_jos[i] in caractere):
                    info = formare_numar(linie_sus,i)
                    sum+=info[1]
                    linie_sus= linie_sus[:info[0]] + "0" * len(str(info[1])) + linie_sus[len(str(info[1]))+info[0]:]
                if (i <len(linie_jos) and linie_jos[i+1]!='.' and  linie_jos[i+1] in caractere):
                    info = formare_numar(linie_sus,i)
                    sum+=info[1]
                    linie_sus= linie_sus[:info[0]] + "0" * len(str(info[1])) + linie_sus[len(str(info[1]))+info[0]:]
            i+=1
        linie_sus = linie_jos
    
    for i in range(len(linie_sus)):
        if(linie_sus[i]!='.'and linie_sus[i] in caractere):
                if (i+1<len(linie_sus) and linie_sus[i+1].isdigit()):
                    info = formare_numar(linie_sus,i+1)
                    sum+=info[1]
                if (i-1>0 and linie_sus[i-1].isdigit()):
                    info = formare_numar(linie_sus,i-1)
                    sum+=info[1]

print("sum=",sum)


                    
                    


