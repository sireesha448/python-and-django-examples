import re
st="this is sireeshas"
res=re.split(r"s",st)
print(res)
print("length of list:",len(res))
print("no of s's:",len(res)-1)
