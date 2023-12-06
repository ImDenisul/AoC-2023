import re

inif =[]
intervale1 = []
intervale2 = []

with open('X:\\Proiecte\\alt proiect\\imput.txt', 'r') as fisier:
    v = fisier.readline()
    v = re.split('[ \n]', v)

    del v[0]
    del v[-1]
    for i in range(0,len(v)-1,2):
        intervale2.append(( int(v[i]), int(v[i]) + int(v[i+1])-1))
    print(intervale2)

    print(v)
    for linie in fisier:
        if(linie[0].isalpha()):
            print(linie)
            i=0
            
            while(i < len(intervale1)):
                intervale2.append((intervale1[i][0],intervale1[i][1]))
                i+=1
            
                

            intervale1 = intervale2
            print(intervale1)
            Nr=0
            for i in intervale1:
                Nr+=i[1]-i[0]+1
            print("Nr elemete",Nr)

            intervale2 = []
        if(linie[0].isalpha() or linie[0]=='\n'):
            continue
        
        linie = re.split('[ \n]', linie)
        if(linie[-1]==''):
            del linie[-1]
        i=0
        while(i<len(intervale1)):
            Start_schiba = int(linie[1])
            End_schiba = int(linie[1])+int(linie[2])
            Start_seed = intervale1[i][0]
            End_seed = (intervale1[i][1])

            diff_stg =Start_seed -Start_schiba
            diff_dr = End_schiba - End_seed

            if(End_schiba<Start_seed or Start_schiba>End_seed):
                inif.append(1)
                i+=1
                continue

            if(diff_stg>=0 and diff_dr>=0):
                inif.append(2)
                intervale2.append((int(linie[0])+diff_stg, int(linie[0])+diff_stg-intervale1[i][0]+intervale1[i][1]))
                del intervale1[i]
            
            if(diff_stg>=0 and diff_dr<0):
                  inif.append(3)
                  intervale2.append((int(linie[0])+diff_stg, int(linie[0])+ int(linie[2])))
                  if(diff_stg!=0):
                      intervale1.append((End_seed+diff_dr+1,End_seed))
                      del intervale1[i]

            if(diff_stg<0 and diff_dr>=0):
                inif.append(4)
                intervale2.append((int(linie[0]), int(linie[0])+int(End_seed-Start_schiba)))
                if(diff_dr!=0):
                    intervale1.append((Start_seed,Start_seed-diff_stg-1))
                    del intervale1[i]
            
            if(diff_stg<0 and diff_dr<0):
                inif.append(5)
                intervale2.append((int(linie[0]), int(linie[0]) + int(linie[2])))
                intervale1.append((Start_seed,Start_seed-diff_stg-1))
                intervale1.append((End_seed+diff_dr+1,End_seed))
                del intervale1[i]
            


        
        

min = intervale1[0][0]              
for i in intervale1:
    if(i[0]<min):
        min = i[0]
print("min=",min)
