import time
a=int(input("n: "))
time.sleep(1)
if a<0:
    print("__Multiplication Table upto_",a,":")
    print("---------------------------------------------------------------------------------")
    time.sleep(1)
    for i in range (-1, a-1, -1):
        print("Table of_",i,":")
        for b in range (1,11):
            print(i,"*",b,"=",i*b)
        print( )
        time.sleep(0.3)
elif(a>0):
    print("__Multiplication Table upto_",a,":")
    print("--------------------------------------------------------------------------------------------------")
    time.sleep(1)
    for i in range(1,a+1):
        print("Table of_",i,":")
        for b in range (1,11):
            print(i,"*",b,"=",i*b)
        print( )
    time.sleep(0.3)
else:
    print("Multiplication Table of",a,":")
    print(0)
