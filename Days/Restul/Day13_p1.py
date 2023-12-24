def oglinda(pattern):
    for i in range(1,len(pattern)):
        sus = pattern[:i][::-1]
        jos = pattern[i:]

        sus = sus[:len(jos)]
        jos = jos[:len(sus)]

        if sus == jos:
            return i
    return 0


with open('X:\\Proiecte\\alt proiect\\imput.txt', 'r') as fisier:
    pattern = fisier.read()
    pattern = pattern.split('\n\n')
    pattern = [x.split('\n') for x in pattern]
    total = 0
    for i in range(len(pattern)):
        total+= oglinda(pattern[i])*100
    pattern2 = []
    for i in range(len(pattern)):
        pattern2= [''.join(s[j]for s in pattern[i]) for j in range(len(pattern[i][0]))]
        total+= oglinda(pattern2)
        
    
    print(total)