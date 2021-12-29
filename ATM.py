import time as t
from datetime import datetime
f=open("TRANSACTIONS.txt","a")
dt=datetime.now().strftime("%d/%b/%Y %H:%M:%S")
f.write("=============================\n")
f.write("Starting the Transactions\n")
f.write(dt)

D={1111:"Ramesh",2222:"Suresh",3333:"Hamesh",4444:"Mahesh"}
M={1111:40000,2222:50000,3333:60000,4444:70000}
C=[[2000,10],[500,12],[100,15],[50,20]]
sum=0

for i in range(len(C)):
    sum=sum+C[i][0]*C[i][1]
f.write("\nAmount available in ATM:")
f.write(str(sum))

def Dispenser(A):
    sum=0
    A=int(A)
    for i in range(len(C)):
        sum=sum+(C[i][0]*C[i][1])
    if A>sum:
        print("\nCash in sufficient, Please visit nearest ATM\n")
        f.write("Requested cash indispensible")
        exit()
    for i in range(len(C)):
        if A==0:
            break
        if C[i][0]*C[i][1] < A :
            A=A-C[i][0]*C[i][1]
            if C[i][1]==0:
                continue
            print(C[i][0],"x",C[i][1], end="+")
            C[i][1]=0
        elif C[i][0]*C[i][1] > A :
            P=A//(C[i][0])
            A=A-C[i][0]*P
            if P==0:
                continue
            print(C[i][0],"x",P, end="+")
            C[i][1]=C[i][1]-P
        elif  C[i][0]*C[i][1] == A:
            P = (C[i][1])
            if P==0:
                continue
            print(C[i][0],"x",P, end="+")
            A=A-C[i][0]*P
            C[i][1]=0
        else:
            print("Error while dispensing",A)
            f.close()
            exit()

print("Welcome to ATM Bank Services")
print("Insert your card")

for i in range(2):
    print("..",end="")
    t.sleep(0.2)
print()

print("Enter your 4 digit PIN")
ac=int(input())

if ac in D:
    print("Hi",'\033[1m','\033[91m',D[ac],'\033[0m') #Red and Bold
    key=1
else:
    print("Wrong A/C number")
    key=0
f.write("\n=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=\n")
f.write(str(ac))
dt=datetime.now().strftime("%d/%b/%Y %H:%M:%S")
f.write(dt)
f.write("   SERVICE OPENED   \n")

while(key):
    L={1:"Balance Enquiry",2:"Money Withdrawl",3:"Exit"}
    print()
    for i in L:
        print(i,":",L[i])
    print("Enter Sl no of the requested service")
    k=int(input())
    if k==1:
        print("Balance:",'\033[1m','\033[94m',M[ac],'\033[0m') #Blue and bold
        dt=datetime.now().strftime("%d/%b/%Y %H:%M:%S")
        f.write(dt)
        f.write("\n")
        f.write(str(ac))
        f.write("   requested Balance enquiry   \n")
        t.sleep(1)
        print("\n=========================\n")
    elif k==2:
        print("enter the amount in multiples of 100")
        A=int(input())
        if A<=M[ac]:
            if A%100==0:
                print()
                for i in range(2):
                    print("..",end="")
                    t.sleep(0.2)
                f=open("TRANSACTIONS.txt","a")
                dt=datetime.now().strftime("%d/%b/%Y %H:%M:%S")
                f.write(dt)
                f.write("\n")
                f.write(str(ac))
                f.write("   requested Cash Withdrawl   \n")
                if A>sum:
                    print("Amount beyond the avaialble cash")
                Dispenser(A)
                M[ac]=M[ac]-A
                dt=datetime.now().strftime("%d/%b/%Y %H:%M:%S")
                f.write(dt)
                f.write("\n")
                f.write(str(ac))
                f.write("   Withdrawl Successful   ")
                f.write(str(A))
                f.write("\n")
            else:
                print("Enter in multiples of 100")
        else:
            print("Not enough money in your account")
    elif k==3:
        dt=datetime.now().strftime("%d/%b/%Y %H:%M:%S")
        f.write(dt)
        f.write("SERVICE CLOSED\n")
        f.write("\n=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=\n")
        f.close()
        exit()
    else:
        print("Invalid Service number requested")
        f.close()