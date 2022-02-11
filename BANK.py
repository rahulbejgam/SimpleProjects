import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["Data1"]
mycol = mydb["Sample"]

def logout():
    print("*************************")
    print("Thank you!!")
    print("*************************")
    exit()

def closeac(q):
    print("Are you sure to close the account?")
    print("1. Yes")
    print("2. No")
    t=int(input("Enter your option: "))
    if t==1:
        print("Collect your balance cash: ")
        mydb1=myclient["Data1"]
        mycol1=mydb1["ATM"]
        query1={"Name": "001"}
        query={"Name":q}
        mydoc1=mycol1.find(query1)
        mydoc=mycol.find(query)
        for i in mydoc:
            A=i["Amount"]
        for i in mydoc1:
            a,b = i["500"], i["2000"]
        sum = a*500 + b*2000
        C=[[2000,b],[500,a]]
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
                print("Error while dispensing")
    else:
        logout()
    query={"Name": q}
    aquery={"$set":{"Status":"C"}}
    mycol.update_one(query, aquery)
    print("Thank you")    

def newac():
    print('Welcome to RBank')
    t=str(input("Pls enter ur name: "))
    d=int(input("Deposit an amount of: "))
    p=str(input("Enter a password: "))
    rp=str(input("Re-enter the password: "))
    m=mycol.find().sort("Account",-1).limit(1)
    for x in m:
        ac = x["Account"]
    if p==rp:
        list={"Name": t, "Amount": d, "Pwd": p, "Account":ac+1, "Status": "A"}
        mycol.insert_one(list)
        print("Account created!!")
        print("Account number: ", ac+1)
    else:
        print("both are not same!, Try again.")

def withdraw(q):
    mydb1=myclient["Data1"]
    mycol1=mydb1["ATM"]
    query1={"Name": "001"}
    query={"Name":q}
    mydoc1=mycol1.find(query1)
    mydoc=mycol.find(query)
    for i in mydoc:
        ava=i["Amount"]
    for i in mydoc1:
       a,b = i["500"], i["2000"]
    sum = a*500 + b*2000
    print("Enter amount to withdraw: ")
    A=int(input())
    B=A
    if (A>ava):
        print("Cash Overflow than Account!")
        logout()
    elif A<500:
        print("Cash less than 500 not dispensible")
        logout()
    else:
        C=[[2000,b],[500,a]]
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
                print("Error while dispensing")
        aquery={"$set":{"500":C[1][1]}}
        bquery={"$set":{"2000":C[0][1]}}
        squery={"$set":{"Amount": ava-B}}
        mycol1.update_one(query1, aquery)
        mycol1.update_one(query1, bquery)
        mycol.update_one(query, squery)     

def auth(t):
    query={"Account": t}
    print(t)
    mydoc=mycol.find(query)
    for x in mydoc:
        if x["Status"] == "C":
            print("Your account was closed!")
            logout()
    print("Enter Password: ")
    t=str(input())
    if t==x["Pwd"] and x["Status"]=="A":
        return 1
    else:
        return 0

def option(t,q):
    query={"Name": q}
    mydoc=mycol.find(query)
    if t==1:
        for x in mydoc:
            print("Balance: ", x["Amount"])
            logout()
    elif t==2:
        for x in mydoc:
            print("Balance: ", x["Amount"])
            old=x["Amount"]
        print("Deposit the cash in the slot")
        try:
            new=int(input("Amount: "))
        except:
            print("Enter a valid amount")
        upquery={"$set":{"Amount":old+new}}
        mycol.update_one(query, upquery)
        logout()
    elif t==3:
        for x in mydoc:
            print("Name: ", x["Name"])
        old=x["Name"]
        new=input("Enter new name: ")
        upquery={"$set":{"Name":new}}
        mycol.update_one(query, upquery)
    elif t==4:
        withdraw(q)
    elif t==5:
        closeac(q)

def services(t):
    query={"Account": t}
    mydoc=mycol.find(query)
    f=0
    for x in mydoc:
        print("Hi",x["Name"],"!")
        f=1
        print("1. Balance Enquiry")
        print("2. Deposit")
        print("3. Update Name")
        print("4. Withdrawl")
        print("5. Close account")
        t=int(input("Enter your service: "))
        option(t, x["Name"])
    if(f<1 or t not in range(1,7)):
        print("Enter valid")

def main():
    print("**************************")
    print("Welcome to RBank")
    print("**************************")
    print("1. Create new account")
    print("2. Account Services")
    print("Choose to proceed")
    try:
        t=int(input())
    except:
        print("Choose between 1 and 2 only")
        logout()
    if t==1:
        print("You chose new account creation!")
        newac()
    elif t==2:
        print("You chose Account Services!")
        print("Enter the Account number to proceed: ")
        t=int(input())
        if(auth(t)):
            services(t)
        else:
            print("Wrong Password!!")
    else:
        print("INVALID OPTION")

main()