import re

NrCari=[1 for i in range(204)]
NrCari[0]=0
ok=0
jocuri_castigate = 0
game1 =0
sum= 0
Nrjoc=0
with open('imput.txt', 'r') as fisier:
    for joc in fisier:
        Nrjoc+=1
        v = re.split('[|]', joc)
        v[0] = re.split('[ \n]', v[0])
        v[1] = re.split('[ \n]', v[1])
        jocuri_castigate=0
        for i in v[0]:
            if(i.isdigit() and i in v[1]):
                jocuri_castigate+=1
        while(jocuri_castigate):
            if(Nrjoc+jocuri_castigate<204):
                NrCari[Nrjoc+jocuri_castigate]+=NrCari[Nrjoc]
            jocuri_castigate-=1

for i in NrCari:
    sum+=i


print(NrCari)
print(game1)
print('sum=',sum)
print('jocuri_castigate',jocuri_castigate)
print('sum=',sum)