with open('imput', 'r') as fisier:
    continut = fisier.read()
    cuvinte = continut.split()
v=[]
sum =0

digits = ['zero0', 'one1', 'two2', 'three3', 'four4', 'five5', 'six6', 'seven7', 'eight8', 'nine9']
digits_bw =['orez0', 'eno1', 'owt2', 'eerht3', 'ruof4', 'evif5', 'xis6', 'neves7', 'thgie8', 'enin9']

potential = []


numbers = []
for cuvant in cuvinte:
    for i in cuvant:
        if i.isdigit():
            v.append(int(i))
            break
        else:
            for j in range( len(digits)) :
                if i ==digits[j][0]:
                 potential.append(digits[j])
            j=0
            while (j < (len(potential))):
                if i == potential[j][0]:
                    potential[j]= potential[j][1:]
                else :
                    potential.remove(potential[j])
                    continue
                if(potential[j][0].isdigit()):
                    v.append(int(potential[j][0]))
                    potential.clear()
                    break
                j+=1
        if(len(v)==1):
            break

    potential.clear()

    for i in reversed(cuvant):
        if i.isdigit():
            v.append(int(i))
            break
        else:
            for j in range( len(digits_bw)) :
                if i ==digits_bw[j][0]:
                 potential.append(digits_bw[j])
            j=0
            while (j <(len(potential))):
                if i == potential[j][0]:
                    potential[j]= potential[j][1:]
                else :
                    potential.remove(potential[j])
                    continue
                if(potential[j][0].isdigit()):
                    v.append(int(potential[j][0]))
                    potential.clear()
                    break

                j+=1
        if(len(v)==2):
            break
    sum += v[0]*10 + v[1]
    potential.clear()
    v.clear()


print(sum)
