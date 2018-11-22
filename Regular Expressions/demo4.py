import re
st="this is sathya technology,technology and technology"
res=re.findall(r"technology",st)
print(res)
print(len(res))
print(type(res))