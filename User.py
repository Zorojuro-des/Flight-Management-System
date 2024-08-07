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
        Ask1 = int(input("How do you want to search: \n 1.Flight number \n 2.Arrival Destination \n Enter the task number:"))
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

        else:
            print("Give a valid input")
        if flag == 1:
            break
        else:
            print("No such flight exists")

def booking():
    f1=open("booking.txt",'r')                                                                   # File ---> Dictionary
    D1 = {}
    i = ' '
    while i != '':
        i = f1.readline()
        while i:
            i2 = i.split(',')
            i2[2] = i2[2].strip('\n')
            D1[i2[0].strip()] = i2
            break
    f1.close()

    while True:
        flag=0
        Ask4=input("For booking-Enter flight number:")                                            # Booking
        a=0
        for i in D1:
            if Ask4==i:
                if int(D1[i][1])>0:
                    a+=1
                    D1[i][1] = str(int(D1[i][1])-1)
                    print("Pay" , D1[i][2] , "rupees at the airport to receive your tickets")
                    flag+=1
                else:
                    print("Sorry!!")
                    print("Tickets are not available for this flight")
        if flag!=0:
            break
        if a==0:
            print("No such flight exists")
            print("Enter a valid flight number")


    f1=open("Booking.txt",'w')                                                   # Updating the booking file
    for i in D1:
        TYPER=D1[i][0]+','+D1[i][1]+','+D1[i][2]+'\n'
        f1.write(TYPER)
    f1.close()

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


b,c,d,e=0,0,0,0
while e == 0:
    Q3 = int(input(
        "These are the options available for you: \n 1.Search a flight \n 2.Book tickets \n 3.Get information of random flight \n 4.Exit \n Enter the task number:"))
    if Q3 == 1:
        while b == 0:
            search()
            Q4 = input("Do you want to search for another flight?(Y/N)").upper()
            if Q4 == 'N':
                b = 1
            elif Q4 == 'Y':
                pass
            else:
                print("Give a valid input")

    elif Q3 == 2:
        while c == 0:
            booking()
            Q5 = input("Do you want to book another ticket?(Y/N)").upper()
            if Q5 == 'N':
                c = 1
            elif Q5 == 'Y':
                pass
            else:
                print("Give a valid input")

    elif Q3 == 3:
        while d == 0:
            update()
            Q6 = input("Do you want to book another ticket?(Y/N)").upper()
            if Q6 == 'N':
                d = 1
            elif Q6 == 'Y':
                pass
            else:
                print("Give a valid input")
    elif Q3 == 4:
        e = 1

    else:
        print("Give a valid input")