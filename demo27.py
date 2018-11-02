big1=0
big2=0
for x in range(1,11):
    no1=int(input("enter number:"))
    if big1>no1:
        print(end="")
    else:
        big1=no1
    if big2<big1 and big2>no1:
        if big1==no1:
            print(end="")
        else:
            big2=no1
    else:
        big2=no1

print(big1,"is a 1st big number")
print(big2,"is a 2nd big number ")