import re




with open('X:\\Proiecte\\alt proiect\\imput.txt', 'r') as fisier:
    v = fisier.readline()
    v = re.split('[ \n]', v)

    del v[0]
    del v[-1]
    print(v)
    ok= [1 for i in range(len(v)+1)]
    for linie in fisier:
        if(linie[0].isalpha()):
            print(linie)
            for i in range(len(ok)):
                ok[i]=1 
        if(linie[0].isalpha() or linie[0]=='\n'):
            continue
        
        linie = re.split('[ \n]', linie)
        if(linie[-1]==''):
            del linie[-1]
        
        for i in range(len(v)):

            if(int(linie[1]) <= int(v[i]) and int(linie[1])+int(linie[2])>= int(v[i]) and ok[i]==1):
                v[i]=int(linie[0]) + (int(v[i])-int(linie [1]))
                ok[i]=0
        print(linie)
        print("v=",v)

min = v[0]                
for i in v:
    if(i<min):
        min = i
print(min)
