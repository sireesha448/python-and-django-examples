no=int(input("enter no:"))
r=no%10
no=no//10
while no!=0:
    r1=no%10
    no=no//10
print("sum is:",r+r1)