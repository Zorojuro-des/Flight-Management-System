f1 = open("airline.txt", 'r')
D1 = {}
i = ' '
while i != '':
  i = f1.readline()
  while i:
    i2 = i.split(' , ')
    i2[5] = i2[5].strip('\n')
    print(i2)
    break
            
