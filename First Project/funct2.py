def chec(num):
    c =0
    a=0
    for x in range(1,num+1,1):
        a += 1 
        if num % x == 0:
            c += 1
    if c == 2:
        print(num, " is prime number \n")
    else : print(num, " is not a prime number \n") 
    print(a)
 
num=int(input("enter a number: "))
chec(num)