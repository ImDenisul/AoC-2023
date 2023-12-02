import re
with open('X:\\Proiecte\\alt proiect\\imput.txt', 'r') as fisier:
    continut = fisier.read()
    jocuri = continut.split('\n')

nr_cuburi= {
    'r':12,
    'b':14,
    'g':13,
}
iduri = []
sum =0
for joc in jocuri:
    ok=1
    v = re.split('[ ]', joc)
    print(v)
    Id = int(v[1][:-1])
    i=2
    while i < len(v):
        if int(v[i])>nr_cuburi[v[i+1][0]]:
             ok=0
        i+=2
    if ok==1:
        iduri.append(Id)
        sum+=Id

print("sum=",sum)
print(iduri)
