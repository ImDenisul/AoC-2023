import re
with open('X:\\Proiecte\\alt proiect\\imput.txt', 'r') as fisier:
    continut = fisier.read()
    jocuri = continut.split('\n')

nr_cuburi= {
    'r':0,
    'b':0,
    'g':0,
}
iduri = []
sum =0
for joc in jocuri:
    v = re.split('[ ]', joc)
    print(v)
    Id = int(v[1][:-1])
    i=2
    while i < len(v):
        if int(v[i])>nr_cuburi[v[i+1][0]]:
                nr_cuburi[v[i+1][0]]=int(v[i])
        i+=2
    sum += nr_cuburi['b']*nr_cuburi['g']*nr_cuburi['r']
    nr_cuburi['r']=0
    nr_cuburi['b']=0
    nr_cuburi['g']=0

print("sum=",sum)
print(iduri)
