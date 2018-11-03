def makes10(no1,no2):
    if no1==10 or no2==10 or no1+no2==10:
        return True
    else:
        return False
no1=int(input("ist no:"))
no2=int(input("2nd no:"))
res=makes10(no1,no2)
print(res)
