def monkey_trouble(a_smile,b_smile):
    if a_smile=="True" and b_smile=="True":
        return True
    elif a_smile=="False" and b_smile=="False":
        return True
    else:
        return False
a_smile=input("enter value")
b_smile=input("enter value")
res=monkey_trouble(a_smile,b_smile)
print(res)