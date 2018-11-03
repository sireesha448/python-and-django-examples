def pos_neg(no1,no2,neg):
    if no1<0 and no2>0 and neg=="False":
        return True
    elif no1>0 and no2<0 and neg=="False":
        return True
    elif no1<0 and no2<0 and neg=="True":
        return True
    else :
        return False
no1=int(input("1st no:"))
no2=int(input("2nd no:"))
neg=input("enter bool value")
res=pos_neg(no1,no2,neg)
print(res)