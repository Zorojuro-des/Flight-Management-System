'''#{Flight no. : List [Flight no. , seats]}
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

    y,x=0,0

    Q1=input("Enter your name:")
    while y==0:
        Q2=int(input("Enter your mobile number:"))
        if len(str(Q2))==10:
            y=1
    Q3=input("Enter your address:")
    while x==0:
        Q4=int(input("Enter your age"))
        if Q4<=120:
            x=1
    Q5=input("Enter date of travel:(DD-MM-YYYY)")

    while True:
        flag=0
        b=0
        while b==0:
            Ask4=input("For booking-Enter flight number:")                                            # Booking
            for i in D1:
                if Ask4 == i:
                    b=1
                else:
                    print("No such flight exists")
                    print("Enter a valid flight number")

        Q6=int(input("How many tickets do you want to book:"))
        for i in D1:
            if Ask4==i:
                if int(D1[i][1])>=Q6:
                    D1[i][1] = str(int(D1[i][1])-Q6)
                    print("Pay" , D1[i][2]*Q6 , "rupees at the airport to receive your tickets")
                    flag+=1
                else:
                    print("Sorry!!")
                    print("Tickets are not available for this flight")

        if flag!=0:
            break

    f1=open("Booking.txt",'w')                                                   # Updating the booking file
    for i in D1:
        TYPER=D1[i][0]+','+D1[i][1]+','+D1[i][2]+'\n'
        f1.write(TYPER)
    f1.close()'''
# {Flight no. : List [Flight no. , seats]}
def booking():
    f1 = open("booking.txt", 'r')  # File ---> Dictionary
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

    z,y, x = 0,0,0

    Q1 = input("Enter your name:")
    while y == 0:
        Q2 = int(input("Enter your mobile number:"))
        if len(str(Q2)) == 10:
            y = 1
        else:
            print()
            print("Give a valid mobile number")
            print()
    Q3 = input("Enter your address:")
    while x == 0:
        Q4 = int(input("Enter your age:"))
        if Q4 <= 120:
            x = 1
        else:
            print()
            print("Give a valid age")
            print()

    while z == 0:
        Q5 = input("Enter date of travel(DD-MM-YYYY):")
        if Q5[:2].isdigit() and Q5[3:5].isdigit() and Q5[6:10].isdigit() and len(Q5) == 10:
            Day = int(Q5[:2])
            Month = int(Q5[3:5])
            Year = int(Q5[6:10])
            if Month == 1 or Month == 3 or Month == 5 or Month == 7 or Month == 8 or Month == 10 or Month == 12:
                if 0 < Day < 32:
                    z = 1

            elif Month == 2:
                if 0 < Day < 29:
                    z = 1

            elif Month == 4 or Month == 6 or Month == 9 or Month == 11:
                if 0 < Day < 31:
                    z = 1

            elif Year <= 999 or 9999 < Year:
                z = 0

            if z == 0:
                print()
                print("Give a valid date")
                print()

        else:
            print()
            print("Give a valid date")
            print()

    while True:
        flag = 0
        a = 0
        Ask4 = input("For booking-Enter flight number:")  # Booking
        Q6 = int(input("How many tickets do you want to book:"))
        for i in D1:
            if Ask4 == i:
                a += 1
                if int(D1[i][1]) >= Q6:
                    D1[i][1] = str(int(D1[i][1]) - Q6)
                    print("Pay", int(D1[i][2]) * Q6, "rupees at the airport to receive your tickets")
                    flag += 1
                else:
                    print("Sorry!!")
                    print("Tickets are not available for this flight")
        if a == 0:
            print("No such flight exists")
            print("Enter a valid flight number")

        if flag != 0:
            break

    f1 = open("airline.txt", 'r')  # File ---> Dictionary
    D2 = {}
    i = ' '
    while i != '':
        i = f1.readline()
        while i:
            i2 = i.split(',')
            i2[2] = i2[2].strip('\n')
            D2[i2[0].strip()] = i2
            break
    f1.close()
    a = len(Q1)
    b = len(Ask4)
    c = len(Q5)
    d = len(D2[Ask4][1])
    e = len(D2[Ask4][2])
    f = len(D2[Ask4][3])

    print("_"*79)
    print("|                             BOARDING PASS                                    |")
    print("|  NAME:", Q1, " " * (68 - a), "|")
    print("|  FROM:", D2[Ask4][1], " " * (33 - d), "TO:", D2[Ask4][2], " "*(29-e), "|")
    print("|  FLIGHT NUMBER:", Ask4, " " * (23-b), "DATE:", Q5 ," "*(28-c),"|" )
    print("|  TIME:",D2[Ask4][3]," "*(68-f),"|" )
    print("_"*79)
    f1 = open("Booking.txt", 'w')  # Updating the booking file

    for i in D1:
        TYPER = D1[i][0] + ',' + D1[i][1] + ',' + D1[i][2] + '\n'
        f1.write(TYPER)
    f1.close()
booking()