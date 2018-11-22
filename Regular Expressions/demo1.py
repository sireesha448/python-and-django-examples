import re
st="this is python assignment"
res=re.match(r"this",st)
print(res)
print(res.group())