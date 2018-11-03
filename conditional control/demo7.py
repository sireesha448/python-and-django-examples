emp=input("enter name:")
sal=float(input("enter salary: "))
desi=input("enter designation:")
bonus=0
if desi=="manager":
    bonus=20*(sal/100)
    sal=sal+bonus
elif desi=="analyst":
    bonus=10*(sal/100)
    sal=sal+bonus
elif desi=="clerk":
    bonus=5*(sal/100)
    sal=sal+bonus
else:
    print("invalid designation entered")
print("total salary is:",sal)


