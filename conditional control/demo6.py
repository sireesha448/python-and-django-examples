bill=0
name=input("enter name:")
stype=input("enter type:")
units=int(input("no of units:"))
if stype=="industy":
    bill=units*5.25
    print(bill)
elif stype=="commersial":
    bill=units*4.00
    print(bill)
elif stype=="residence":
    bill=units*3.08
    print(bill)
else:
    print("you are entered invalid type")

