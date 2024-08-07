f1 = open("airline.txt", 'r')  # File ---> Dictionary
D1 = {}
i = ' '
while i != '':
    i = f1.readline()
    while i:
        i2 = i.split(',')
        i2[5] = i2[5].strip('\n')
        D1[i2[0].strip()] = i2
        break
f1.close()
Q=input("Enter the flight number of flight to be deleted:")
D2={}
for i in D1:
    if i==Q:
        pass
    else:
        D2[i]=D1[i]

f1=open("airline.txt", 'w')
for j in D2:
    L=D2[j]
    TYPER=L[0]+' , '+L[1]+' , '+L[2]+' , '+L[3]+' , '+L[4]+' , '+L[5]+'\n'
    f1.write(TYPER)
f1.close()
print("The flight number",Q,"has been deleted from the records")