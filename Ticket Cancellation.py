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

    a=0
    Q1=input("Enter your name:")
    while a==0:
        Q2=int(input("Enter your mobile number:"))
        if len(str(Q2))==10:
            a=1
    b = 0
    while b == 0:
        Q3 = input("For booking-Enter flight number:")  # Booking
        for i in D1:
            if Q3 == i:
                b = 1
            else:
                print("No such flight exists")
                print("Enter a valid flight number")

    Q4=int(input("Enter how many tickets do you want to cancel:"))
    Q5 = input("Enter date of travel:(DD-MM-YYYY)")

    for i in D1:
        if Q3 == i:
            D1[i][1]+=Q4

    f1 = open("Booking.txt", 'w')                            # Updating the booking file
    for i in D1:
        TYPER = D1[i][0] + ',' + D1[i][1] + ',' + D1[i][2] + '\n'
        f1.write(TYPER)
    f1.close()