import re
st="naveen sir python class"
res=re.match(r"naveen",st)
print(res)
print(type(res))
print(res.start())
print(res.end())