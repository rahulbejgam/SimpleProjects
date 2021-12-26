sum=0
md=idli=wd=idli=tea=od=pori=0
for i in range(1,50):
        print("1.MASALA DOSA-30 2.IDLI-30 3.WADA-30 4.PORI-25 5.ONION DOSA-35 6.TEA-10 7.MONEY")
        ptr=int(input())
        print(ptr)
        if ptr==1:
            sum+=30
            print("MASALA DOSA=30")
            md+=1
            f = open("HOTEL.txt", "a")
            f.write("MASALA DOSA\n")
            f.close()
        elif ptr==2:
            sum+=30
            print("IDLI=30")
            idli+=1
            f = open("HOTEL.txt", "a")
            f.write("IDLI\n")
            f.close()
        elif ptr==3:
            sum+=30
            print("WADA=30")
            wd+=1
            f = open("HOTEL.txt", "a")
            f.write("WADA\n")
            f.close()
        elif ptr==4:
            sum+=25
            print("PORI=30")
            pori+=1
            f = open("HOTEL.txt", "a")
            f.write("PORI\n")
            f.close()
        elif ptr==5:
            sum+=35
            print("ONION DOSA=35")
            od+=1
            f = open("HOTEL.txt", "a")
            f.write("ONION DOSA\n")
            f.close()
        elif ptr==6:
            sum+=10
            print("TEA=10")
            tea+=1
            f = open("HOTEL.txt", "a")
            f.write("TEA\n")
            f.close()
        elif (ptr==7):
            print(sum)
            print("MASALA DOSA=",md)
            print("ONION DOSA=",od)
            print("TEA=",tea)
            print("IDLI=",idli)
            print("WADA=",wd)
            print("PORI=",pori)
            break
