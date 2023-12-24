with open('X:\\Proiecte\\alt proiect\\imput.txt', 'r') as fisier:
    sum =0 
    k=0
    sir= fisier.read().split(',')
    for i in range(len(sir)):
        k=0
        for j in range(len(sir[i])):
            k+=ord(sir[i][j])
            k*=17
            k%=256
        sum+=k
print(sum)