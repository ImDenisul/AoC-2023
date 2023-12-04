import re

ok=0
jocuri_castigate = 0
game1 =0
sum= 0
with open('X:\\Proiecte\\alt proiect\\imput.txt', 'r') as fisier:
    for joc in fisier:
        v = re.split('[|]', joc)
        v[0] = re.split('[ \n]', v[0])
        v[1] = re.split('[ \n]', v[1])
        jocuri_castigate=0
        for i in v[0]:
            if(i.isdigit() and i in v[1]):
                jocuri_castigate+=1
        if(jocuri_castigate!=0):
            sum+=2**(jocuri_castigate-1)

print(game1)
print('sum=',sum)
print('jocuri_castigate',jocuri_castigate)
print('sum=',sum)