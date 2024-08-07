def search():
    f1 = open("airline.txt", 'r')                                   # Opening the info file
    D1 = {}
    i = ' '
    while i != '':                                              # File ---> Dictionary
        i = f1.readline()
        while i:
            i2 = i.split(' , ')
            i2[5] = i2[5].strip('\n')
            D1[i2[0].strip()] = i2
            break
    while True:                                                                 # Searching the flight
        flag = 0
        Ask1 = int(input("How do you want to search: \n 1.Flight number \n 2.Arrival Destination \n 3.Departure Destination \n Enter the task number:"))
        if Ask1 == 1:
            Q1 = input("Enter flight number:")
            for j in D1:
                if Q1 == j:
                    print(D1[j])
                    flag = 1

        elif Ask1 == 2:
            Q1 = input("Enter arrival destination:").upper()
            for k in D1:
                if Q1 == D1[k][2].strip():
                    print(D1[k])
                    flag = 1

        elif Ask1 == 3:
            Q1 = input("Enter arrival destination:").upper()
            for l in D1:
                if Q1 == D1[l][2].strip():
                    print(D1[l])
                    flag = 1

        else:
            print("Give a valid input")
        if flag == 1:
            break
        else:
            print("No such flight exists")