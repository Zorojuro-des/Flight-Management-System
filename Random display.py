import random
def update():
    f1 = open("random.txt", 'r')                                        # Opening the update file
    D1 = {}
    i = ' '
    while i != '':
        i = f1.readline()
        while i:
            i2 = i.split(' , ')
            i2[5] = i2[5].strip('\n')
            D1[i2[0].strip()] = i2
            break
    f1.close()
    flag=0
    while flag==0:
        R1=D1.popitem()
        R2=list(R1)
        R3='Flight number '+R2[1][0]+' will take off from '+R2[1][1]+' at '+R2[1][3]+' and will land in '+R2[1][2]+' at '+R2[1][4]+'\n'+'The flight type is '+R2[1][5]
        print(R3)
        flag=1
    f1 = open("random.txt", 'w')
    for j in D1:
        L = D1[j]
        TYPER = L[0] + ' , ' + L[1] + ' , ' + L[2] + ' , ' + L[3] + ' , ' + L[4] + ' , ' + L[5] + '\n'
        f1.write(TYPER)
    f1.close()
update()