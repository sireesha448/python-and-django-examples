pn=0
for x in range(1,10):
    no=int(input("enter number"))
    for y in range(2,no):
        if (no%y)==0:
            print(end="")
            break
    else:
        pn+=1
print("no of prime numbers:",pn)