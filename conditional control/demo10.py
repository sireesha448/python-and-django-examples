def parrot_trouble(value,hour):
    if hour>=0 and hour<=23:
        if hour<7 or hour>20 and value=="True":
            return True
        else:
            return False
hour=int(input("enter hour:"))
value=input("enter value:")
res=parrot_trouble(value,hour)
print(res)