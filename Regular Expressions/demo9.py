import re
st="this$%%% is @ python #448 \n Sireesha"
#st="this is python"
res=re.findall(r"\w*",st)
print(res)
print("===================================")
res=re.findall(r"\W*",st)
print(res)
print("===================================")
res=re.findall(r"\w+",st)
print(res)
print("===================================")
res=re.findall(r"\W+",st)
print(res)




