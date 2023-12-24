def HASH(sir):
    sum =0 
    k=0
    for j in range(len(sir)):
        k+=ord(sir[j])
        k*=17
        k%=256
    return k


with open('X:\\Proiecte\\alt proiect\\imput.txt', 'r') as fisier:
    sir = fisier.read().split(',')
    cuti ={}
    for i in range(len(sir)):
        index =sir[i].find('=')
        if index!=-1:
            cutie =HASH(sir[i][:index])
            if cutie in cuti:
                #cautam daca exista deja un tuplu cu acelasi nume si il inlocuim 
                for j in range(len(cuti[cutie])):
                    if cuti[cutie][j][0]==sir[i][:index]:
                        cuti[cutie][j]=(sir[i][:index], int(sir[i][index+1:]))
                        break
                else:
                    cuti[cutie].append((sir[i][:index], int(sir[i][index+1:])))
            else:
                cuti[cutie]=[(sir[i][:index], int(sir[i][index+1:]))]
        index =sir[i].find('-')
        if index!=-1:
            cutie =HASH(sir[i][:index])
            if cutie in cuti:
                #gaseste tuplul care are acelasi nume si stergeti-l
                for j in range(len(cuti[cutie])):
                    if cuti[cutie][j][0]==sir[i][:index]:
                        cuti[cutie].pop(j)
                        break
    sum=0
    for i in cuti:
        for j in range(len(cuti[i])):
            sum+= (i+1) * (j+1)* cuti[i][j][1]
        

    print(cuti)
    print(sum)