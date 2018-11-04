no=int(input("enter a number"))
for x in range(2,no):
    if no%x==0:
        print(no,"is not a prime number")
        break
else:
    print(no,"is a prime number")
