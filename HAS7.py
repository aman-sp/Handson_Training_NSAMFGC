n=[1,1,1,2,2,3]
x=2
d={}
for k in set(n):
    d[k]=0
for j in n:
    d[j]+=1
print(d)
keys,values=[],[]
for key,val in d.items():
    keys.append(key)
    values.append(val)
print(keys)
print(values)
top=[]
for el in sorted(values)[-x:]:
    top.append(keys[values.index(el)])
print(sorted(top))