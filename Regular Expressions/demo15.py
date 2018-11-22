import re
user_name=input("enter name:")
res=re.match(r"^[A-Za-z]*$",user_name)
if res==None:
    print("invalid string")
else:
    print("welcome miss/mr.",user_name)