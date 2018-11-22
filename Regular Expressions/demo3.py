import re
st="this is sathya technology,technology and technology"
res=re.search(r"technology",st)
print(res)
print(type(res))
print(res.group())