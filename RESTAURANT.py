import time as s
from datetime import datetime
ft = datetime.now().strftime("%d/%m/%Y")
dt = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
sum=0
f = open("BILLDETAILS.txt", "a")
f.write(ft)
f.write("\n")
f.write("\nGetting Business Back")
f.write("\n")
while(1):
    print()
    print("********************************")
    print("Welcome to the Restaurant")
    k={1:"idli - 30 INR",2:"dosa - 45 INR",3:"coffee - 15 INR",4:"tea - 10 INR",5:"pizza - 60 INR",6:"sandwich - 50 INR",7:"burger - 100 INR"}
    for i in k:
        print(i,":",k[i])
    print("Select the item from the above list and enter the number")
    ind=(input())
    if not ind.isdigit():
        print("Invalid Input, Insert the Sl.no against your choice ")
        f.write("*\*\*\*\*\*\*\ EXITED HERE DUE TO WRONG I/O /*/*/*/*/*/*/*/*/*\n")
        exit()
    ind=int(ind)
    if ind>7 or ind<1:
        print("choose an item from the given list only")
        ind=int(input())
        if ind>7 or ind<1:
            print("You have chose the invalid item")
            print("Please call for assistance")
            print("**********************************")
            f.write("*\*\*\*\*\*\*\EXITED HERE/*/*/*/*/*/*/*/*/*\n")
            exit()
    else:
        print("You have selected", k[ind].strip("- INR0123456789"))
    print("Processing the order\n")
    for i in range(4):
        print("..",end="")
        s.sleep(0.5)
    print("Collect your order and Bill")
    print("\n******BILL RECEIPT******")
    print(dt)
    print("Item: ", k[ind].strip("- INR0123456789\n"))
    print("Amount:",k[ind].strip("- INR abcdefghijklmnopqrstuvwxyz"),"\n")
    f = open("BILLDETAILS.txt", "a")
    dt = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    f.write(dt)
    f.write("\n")
    f.write(k[ind].strip("- INR0123456789"))
    f.write("\n")
    f.write(k[ind].strip("- INRabcdefghijklmnopqrstuvwxyz"))
    sum=sum+int(k[ind].strip("- INRabcdefghijklmnopqrstuvwxyz"))
    f.write("\nTotal Cash in:")
    f.write(str(sum))
    f.write("\n")
    f.write("====================\n")
    print("       THANK YOU")
    print("****** VISIT AGAIN ********")
    s.sleep(0.9)