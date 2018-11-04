Pno=0
Nno=0
for x in range(1,11):
    no = int(input("enter number:"))
    if no>=1:
        Pno+=1
    else:
        Nno+=1
print("no of +ve numbers: ",Pno)
print("no of -ve numbers:",Nno)