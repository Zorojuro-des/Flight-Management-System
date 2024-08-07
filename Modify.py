#D={Flight number : List[Flight no. , dep dest , arr dest , dep time , arr time , flight type]}
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
Modify()