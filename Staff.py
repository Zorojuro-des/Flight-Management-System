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
    print(D1)
    while True:
        if c!=0:
            break
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


f,g,h,i=0,0,0,0
for i in range(0, 3):
    Q2 = input("Enter the password:")
    if Q2 == "STAFF123#":
        while f == 0:
            Q7 = int(input("These are the options available for you: \n "
                           "1.Add information of new flight \n "
                           "2.Update information of a flight \n "
                           "3.Book ticket \n 4.Exit \n Enter the task number:"))

            if Q7 == 1:
                while g == 0:
                    create()
                    Q8 = input("Do you want to add another flight?(Y/N)").upper()
                    if Q8 == 'Y':
                        pass
                    elif Q8 == 'N':
                        g = 1
                    else:
                        print("Give a valid input")

            elif Q7 == 2:
                while h == 0:
                    Modify()
                    Q9 = input("Do you want to change information of another flight?(Y/N)").upper()
                    if Q9 == 'Y':
                        pass
                    elif Q9 == 'N':
                        h = 1
                    else:
                        print("Give a valid input")

            elif Q7 == 3:
                while i == 0:
                    booking()
                    Q10 = input("Do you want to book ticket for another person?(Y?N)").upper()
                    if Q10 == 'Y':
                        pass
                    elif Q10 == 'N':
                        i = 1
                    else:
                        print("Give a valid input")

            elif Q7 == 4:
                f = 1

            else:
                print("Give a valid input")

        break