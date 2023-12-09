ordine = {'A':13,'K':12,'Q':11,'J':0,'T':9,'9':8,'8':7,'7':6,'6':5,'5':4,'4':3,'3':2,'2':1}
def functie_sortare(tupluri):
    def cheie_de_sortare(tuplu):
        return (tuplu[0], [ordine[c] for c in tuplu[1]])

    return sorted(tupluri, key=cheie_de_sortare)

frecventa = {}
Rank_carti = []
with open('import.txt', 'r') as fisier:
    for v in fisier:
        v =v.split()
        print(v)
        for i in v[0]:
            if(i in frecventa.keys()):
                frecventa[i]+=1
            else:
                frecventa[i]=1
        Nr_identice = 0
        tip = 0
        for i in frecventa:
            if(frecventa[i]>Nr_identice):
                if(i != 'J'):
                    Nr_identice = frecventa[i]
                    cheie = i
        if('J' in frecventa.keys() and Nr_identice!=0):
            frecventa[cheie]+= frecventa['J']
            Nr_identice = frecventa[cheie]
            del frecventa['J']
        if(Nr_identice==0):
            Nr_identice = 5

        if((Nr_identice==3 and len(frecventa) ==2) or Nr_identice>3):
            tip = Nr_identice+2
        if(len(frecventa)==3 and Nr_identice==3):
            tip = 4

        if(len(frecventa)==3 and Nr_identice==2):
            tip = 3
        if(tip==0):
            tip = Nr_identice
        print(tip)
        del frecventa
        frecventa = {}
        Rank_carti.append((tip, v[0], v[1]))

        print(Nr_identice)
        print(frecventa)

    Rank_carti = functie_sortare(Rank_carti)


    print(Rank_carti)
    rez= 0
    for i in range(0, len(Rank_carti)):
        rez += int(Rank_carti[i][2]) * (i+1)
    print(rez)







