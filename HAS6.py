wrds=["listen","silent","enlist","rat","tar","art","cat","act"]
sorted_w=[''.join(sorted(i)) for i in wrds]
d={}
for k in sorted(set(sorted_w)):
    d[k]=[]
cnt=0
for i in sorted_w:
    d[i].append(wrds[cnt])
    cnt+=1
print(d)