C=[[2000,10],[500,12],[200,15],[100,17],[50,20]]

def Dispenser(A):
    if A.isdigit() and int(A)%100==0:
        A=int(A)

    else:
        print("Enter a valid amount in multiples of 100")
        exit()
    s=0
    for i in range(len(C)):
        s=s+C[i][0]*C[i][1]

    if A>s:
        print("Requested amount not available")
        exit()

    for i in range(len(C)):
        if A==0:
            break

        if C[i][1]==0:
            continue

        if C[i][0]*C[i][1] < A :
            A=A-(C[i][0]*C[i][1])
            print(C[i][0],"*",C[i][1], end="+")
            C[i][1]=0

        elif C[i][0]*C[i][1] > A :
            P=A//(C[i][0])
            A=A-C[i][0]*P
            if P==0:
                continue
            print(C[i][0],"*",P, end="+")
            C[i][1]=C[i][1]-P

        elif  C[i][0]*C[i][1] == A:
            P = (C[i][1])
            if P==0:
                continue
            print(C[i][0],"*",P, end="+")
            A=A-C[i][0]*P
            C[i][1]=0

        else:
            print("Error while dispensing",A)
            exit()
while(1):
    Amount=(input("\nEnter the amount to dispense: "))
    Dispenser(Amount) 
