import re

data = []

for i in data:
  m = re.search("^[a-zA-Z0-9_]*$", i)
  if m==None:
    data.remove(i)
    
data2 = [i for i in data if not i.isalpha()]

data3 = []

for k in data2:
    if len(k)==5:
        data3 = data3 + [k]