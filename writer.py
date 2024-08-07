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
    l,m=0,0
    while True:
        while l==0:
            dep_time = input("Enter departure time:")
            if int(dep_time[:1])>24:
                pass
            elif int(dep_time[3:])>=60:
                pass
            else:
                l=1
        while m==0:
            arr_time = input("Enter arrival time:")
            if int(arr_time[:1])>24:
                pass
            elif int(arr_time[3:])>=60:
                pass
            else:
                l=1
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


create()
