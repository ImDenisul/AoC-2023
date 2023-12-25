
class Node:
    def __init__(self, cat ,semn=None, val= None,workflow=None):
        swich = {
            'x':0,
            'm':1,
            'a':2,
            's':3
        }
        self.val = int(val)
        self.cat = swich[cat]
        if semn == '>':
            self.semn = True
        elif semn == '<':
            self.semn = False
        self.workflow = workflow
        self.next = None

class ListaF:
    def __init__(self):
        self.head = None



with open('X:\\Proiecte\\alt proiect\\imput.txt', 'r') as fisier:
    date = fisier.read()
    P= []
    F ={}
    filtre , parti = date.split('\n\n')
    filtre = filtre.split('\n')
    parti = parti.split('\n')
    parti = [i[1:-1] for i in parti]
    parti = [i.split(',') for i in parti]
    for i in range(len(parti)):
        #          x                m               a              s
        P.append((int(parti[i][0][2:]),int(parti[i][1][2:]), int(parti[i][2][2:]), int(parti[i][3][2:])))

    filtre = [i.split('{') for i in filtre]
    # print(filtre)
    for fi in filtre:
        F[fi[0]] = ListaF()

    for fi in filtre:
       
       fi[1] = fi[1].split(',')
       fi[1][-1] = fi[1][-1][:-1]
    #    print(fi)
       index = fi[1][0].index(':')
       curent = Node(fi[1][0][0],fi[1][0][1],fi[1][0][2:index],fi[1][0][index+1:])
       F[fi[0]].head = curent
       for i in range(1,len(fi[1])):
            if ':' in fi[1][i]:
                index = fi[1][i].index(':')
            if len(fi[1][i])>2 and (fi[1][i][1]=="<" or fi[1][i][1]==">"):
               curent.next = Node(fi[1][i][0],fi[1][i][1],fi[1][i][2:index],fi[1][i][index+1:])
               curent = curent.next
            else:
               curent.next = Node('x','>','0',fi[1][i])
    
    for i in F:
        curent = F[i].head
        while curent != None:
            print(curent.cat,curent.semn,curent.val,curent.workflow)
            curent = curent.next
        print('-------------------')
    
    F['A'] = ListaF()
    F['A'].head = Node('x','<','0','Acceptat')
    F['R'] = ListaF()
    F['R'].head = Node('x','<','0','Respins')

    rezultate = []
    for i in P:
        curent = F['in'].head
        while curent.workflow != 'Acceptat' and curent.workflow !='Respins':
            if ((i[curent.cat] >= curent.val) == curent.semn):
                curent = F[curent.workflow].head
            else:
                curent = curent.next
        if curent.workflow == 'Acceptat':
            rezultate.append(i)
    for i in rezultate:
        print(i)

    suma = 0
    for i in rezultate:
        suma += i[0] + i[1] + i[2] + i[3]
    print(suma)
               

       
        
   
    