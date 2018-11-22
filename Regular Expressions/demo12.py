import re
st="this#$ is$% sathya technology"

res=re.findall(r"[aeiouAEIOU]\w+",st)
print(res)
print("=============")
res=re.findall(r"[aeiouAEIOU]\w*",st)
print(res)
res=re.findall(r"[#$%&^@]\W+",st)
print(res)