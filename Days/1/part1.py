with open('imput', 'r') as fisier:
    continut = fisier.read()
    cuvinte = continut.split()
v=[]
sum =0
for cuvant in cuvinte:
    for i in cuvant:
        if i.isdigit():
            if len(v)==0:
                v.append(int(i))
                v.append(int(i))
            else:
                v[1]=int(i)
    sum += v[0]*10 + v[1]
    v.clear()


print(sum)