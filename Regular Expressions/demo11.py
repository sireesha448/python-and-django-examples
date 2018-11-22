import re
st="this$ is @ python #448\n Sireesha"

res=re.findall(r"\w\w",st)
print(res)
print("===================================")
res=re.findall(r"\W\W",st)
print(res)
print("===================================")
res=re.findall(r"\b\w",st)
print(res)
print("===================================")
res=re.findall(r"\b\W",st)
print(res)

