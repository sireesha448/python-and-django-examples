evenno=0
oddno=0
for x in range(1,11):
    no=int(input("enter number:"))
    if (no%2)==0:
        evenno+=1
    else:
        oddno+=1
print("no of even numbers",evenno)
print("no of even numbers",oddno)


