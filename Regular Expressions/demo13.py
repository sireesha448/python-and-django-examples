import re
st="sireesha@gmail.com siri@yahoo.in"
res=re.findall(r"@\w*",st)
res1=re.findall(r"@\w+",st)
print(res)
print(res1)
print("=============================")

res=re.findall(r"@\w*.\w*",st)
res1=re.findall(r"@\w+.\w+",st)
print(res)
print(res1)
print("=============================")

res=re.findall(r"@\w+.(\w*)",st)
res1=re.findall(r"@\w+.(\w+)",st)
print(res)
print(res1)