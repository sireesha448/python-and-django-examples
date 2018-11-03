def sum_double(no1,no2):
    if no1!=no2:
        return no1+no2
    else:
        return 2*(no1+no2)
no1=int(input("1st no:"))
no2=int(input("2nd no:"))
res=sum_double(no1,no2)
print(res)