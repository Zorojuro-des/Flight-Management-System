import random

def delete():
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
    Q = input("Enter the flight number of flight to be deleted:")
    D2 = {}
    for i in D1:
        if i == Q:
            pass
        else:
            D2[i] = D1[i]

    f1 = open("airline.txt", 'w')
    for j in D2:
        L = D2[j]
        TYPER = L[0] + ' , ' + L[1] + ' , ' + L[2] + ' , ' + L[3] + ' , ' + L[4] + ' , ' + L[5] + '\n'
        f1.write(TYPER)
    f1.close()
    print("The flight number", Q, "has been deleted from the records")

def Cancel():
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

    a = 0
    Q1 = input("Enter your name:")
    while a == 0:
        Q2 = int(input("Enter your mobile number:"))
        if len(str(Q2)) == 10:
            a = 1
        else:
            print("Enter a valid mobile number")
    b = 0
    while b == 0:
        Q3 = input("For canceling-Enter flight number:")  # Booking
        for i in D1:
            if Q3 == i:
                b = 1
            if b==1:
                break
        else:
            print("No such flight exists")
            print("Enter a valid flight number")

    Q4 = int(input("Enter how many tickets do you want to cancel:"))

    for i in D1:
        if Q3 == i:
            D1[i][1]=int(D1[i][1])+Q4

    f1 = open("Booking.txt", 'w')  # Updating the booking file
    for i in D1:
        TYPER = D1[i][0] + ',' + str(D1[i][1]) + ',' + D1[i][2] + '\n'
        f1.write(TYPER)
    f1.close()

def create():
    f1 = open("airline.txt", 'a')
    while True:
        flight_number = int(input("Enter flight number:"))
        if 999 >= flight_number >= 100:
            break
        else:
            print("Flight number should be a 3-digit number")

    while True:
        dep_dest = input("Enter departure destination:").upper()
        arr_dest = input("Enter arrival destination:").upper()
        if dep_dest == arr_dest:
            print("Departure destination should not coincide with arrival destination")
        else:
            break

    while True:
        dep_time = input("Enter departure time:")
        arr_time = input("Enter arrival time:")
        if dep_time == arr_time:
            print("Departure time should not be equal to arrival time")
        else:
            break

    while True:
        flight_type = int(input("Enter: \n 1 if flight is Boeing  \n 2 if flight is Airbus"))
        if flight_type == 1:
            a = int(input("Enter flight type number:"))
            FT = 'B' + str(a)
            break
        elif flight_type == 2:
            a = int(input("Enter flight type number:"))
            FT = 'A' + str(a)
            break
        else:
            print("Give a valid input")

    fw = str(flight_number) + " , " + dep_dest + " , " + arr_dest + " , " + dep_time + " , " + arr_time + " , " + FT +'\n'       #Adding in the file for main info
    f1.write(fw)
    f1.close()

    f2=open("booking.txt",'a')                                                          # Adding in the file for booking

    seat_number=int(input("Enter no of seats="))
    flight_price=int(input("Enter cost of flight="))
    Sum=str(flight_number)+","+str(seat_number)+","+str(flight_price)+'\n'

    f2.write(Sum)
    f2.close()

    f3=open("random.txt",'a')                                                           # Adding in the file for update

    fw = str(flight_number) + " , " + dep_dest + " , " + arr_dest + " , " + dep_time + " , " + arr_time + " , " + FT + '\n'
    f3.write(fw)
    f3.close()

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

def display_all():
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
    print(['Flight number','Departure Destination','Arrival Destination','Departure time','Arrival time','Flight type'])
    for i in D1:
        print(D1[i])

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

def Modify():
    f1=open("airline.txt",'r')
    D1 = {}
    i = ' '
    while i != '':                                                      # File ---> Dictionary
        i = f1.readline()
        while i:
            i2 = i.split(' , ')
            i2[5] = i2[5].strip('\n')
            D1[i2[0].strip()] = i2
            break
    f1.close()
    f1=open("airline.txt",'w')
    c=0
    while c==0:
        Ask2=input("Enter the flight number:").strip()

        for i in D1:
            if i == Ask2:
                while True:
                    b=0
                    Ask3=int(input("Enter what do you want to modify \n 1. Departure Destination \n 2. Arrival Destination \n 3. Departure Time \n 4. Arrival Time \n 5.Go Back \n Enter the task number:"))

                    while True:
                        a=0
                        if Ask3==1:                                                                          # Modify Departure destination
                            Dep_D_E=input("Enter the new departure destination:").upper()
                            if Dep_D_E==D1[i][1]:
                                print("You entered the same destination")
                            elif Dep_D_E==D1[i][2]:
                                print("Departure destination should not coincide with arrival destination")
                            else:
                                D1[i][1]=Dep_D_E
                                a+=1
                        else:
                            break
                        if a==1:
                            break

                    while True:
                        a=0
                        if Ask3==2:                                                                         # Modify Arrival Destination
                            Arr_D_E=input("Enter the new arrival destination:").upper()
                            if Arr_D_E==D1[i][2]:
                                print("You entered the same destination")
                            elif Arr_D_E==D1[i][1]:
                                print("Departure destination should not coincide with arrival destination")
                            else:
                                D1[i][2]=Arr_D_E
                                a+=1
                        else:
                            break
                        if a==1:
                            break

                    while True:
                        a=0
                        if Ask3==3:
                            Dep_E=input("Enter the new departure time:")                            # Modify Departure Time
                            if Dep_E==D1[i][3]:
                                print("You entered the same time")
                            elif Dep_E==D1[i][4]:
                                print("Departure time should not be equal to arrival time")
                            else:
                                D1[i][1]=Dep_E
                                a+=1
                        else:
                            break
                        if a==1:
                            break

                    while True:
                        a=0
                        if Ask3==4:
                            Arr_E=input("Enter the new arrival time:")                            # Modify Arrival Time
                            if Arr_E==D1[i][4]:
                                print("You entered the same time")
                            elif Arr_E==D1[i][3]:
                                print("Departure time should not be equal to arrival time")
                            else:
                                D1[i][1]=Arr_E
                                a+=1
                        else:
                            break
                        if a==1:
                            break

                    if Ask3==5:                                                                 # Go back
                        b+=1
                        c+=1

                    if b==1:
                        break

                    if Ask3 !=1 and Ask3 !=2 and Ask3 !=3 and Ask3 !=4 and Ask3 !=5:
                        print("Give a valid input.")
    for j in D1:
        L=D1[j]
        TYPER=L[0]+' , '+L[1]+' , '+L[2]+' , '+L[3]+' , '+L[4]+' , '+L[5]+'\n'
        f1.write(TYPER)
    f1.close()


print("Hello!! Welcome to COSMOS airlines")
a=0
while a==0:                                                                  #Main loop
    Q1=input("Enter if you are a \n User(U) \n Staff member(S) \n Exit(E):").upper()            #Who is the user
    if Q1=="U":                                                           #User code
        e=0
        while e==0:
            Q3=int(input("These are the options available for you: \n 1.Search a flight \n 2.Book tickets \n 3.Cancel tickets \n 4.Display all flights \n 5.Exit \n Enter the task number:"))
            if Q3==1:
                b=0
                while b==0:
                    search()
                    j=0
                    while j==0:
                        Q4=input("Do you want to search for another flight?(Y/N)").upper()
                        if Q4=='N':
                            b=1
                            j=1
                        elif Q4=='Y':
                            j=1
                        else:
                            print("Give a valid input")

            elif Q3==2:
                c=0
                while c==0:
                    booking()
                    k=0
                    while k==0:
                        Q5 = input("Do you want to book another ticket?(Y/N)").upper()
                        if Q5 == 'N':
                            k=1
                            c = 1
                        elif Q5 == 'Y':
                            k=1
                        else:
                            print("Give a valid input")

            elif Q3==4:
                display_all()

            elif Q3==5:
                e=1

            elif Q3==3:
                p=0
                while p==0:
                    Cancel()
                    q=0
                    while q==0:
                        Q7 = input("Do you want to cancel another ticket?(Y/N)").upper()
                        if Q7 == 'N':
                            q=1
                            p=1
                        elif Q7 == 'Y':
                            q=1
                        else:
                            print("Give a valid input")

            else:
                print("Give a valid input")

    elif Q1=="S":                                                        #Staff code
        for i in range(0,3):
            Q2 = input("Enter the password:")
            if Q2=="STAFF123#":
                f=0
                while f==0:
                    Q7=int(input("These are the options available for you: \n "
                             "1.Add information of new flight \n "
                             "2.Update information of a flight \n "
                             "3.Book ticket \n 4.Cancel a ticket \n 5.Display all flights \n 6.Delete a flight \n 7.Exit \n Enter the task number:"))

                    if Q7==1:
                        g=0
                        while g==0:
                            create()
                            m=0
                            while m==0:
                                Q8=input("Do you want to add another flight?(Y/N)").upper()
                                if Q8=='Y':
                                    m=1
                                elif Q8=='N':
                                    g=1
                                    m=1
                                else:
                                    print("Give a valid input")

                    elif Q7==2:
                        h=0
                        while h==0:
                            Modify()
                            n=0
                            while n==0:
                                Q9=input("Do you want to change information of another flight?(Y/N)").upper()
                                if Q9=='Y':
                                    n=1
                                elif Q9=='N':
                                    h=1
                                    n=1
                                else:
                                    print("Give a valid input")

                    elif Q7==3:
                        z=0
                        while z==0:
                            booking()
                            o=0
                            while o==0:
                                Q10=input("Do you want to book ticket for another person?(Y?N)").upper()
                                if Q10=='Y':
                                    o=1
                                elif Q10=='N':
                                    i=1
                                    o=1
                                else:
                                    print("Give a valid input")

                    elif Q7==7:
                        f=1

                    elif Q7==5:
                        display_all()

                    elif Q7==6:
                        z=0
                        while z==0:
                            delete()
                            y=0
                            while y==0:
                                Q11=input("Do you want to delete another flight? (Y/N)").upper()
                                if Q11=='Y':
                                    y=1
                                elif Q11=='N':
                                    y=1
                                    z=1
                                else:
                                    print("Give valid input")


                    elif Q7 == 3:
                        r=0
                        while r == 0:
                            Cancel()
                            s=0
                            while s == 0:
                                Q8 = input("Do you want to cancel another ticket?(Y/N)").upper()
                                if Q8 == 'N':
                                    r = 1
                                    s = 1
                                elif Q8 == 'Y':
                                    s = 1
                                else:
                                    print("Give a valid input")

                    else:
                        print("Give a valid input")

                break
            else:
                print("Enter the correct password.")
        else:
            a+=1

    elif Q1=='E':
        a=1

    else:
        print("Give a valid input")



print("Thank you for using our program.")
print("Have a great day")
# Airline management program made by Tapash Darji(Class-11 A , Roll No.- 18) and     Sona Jain(Class-11 A , Roll No.- 10)