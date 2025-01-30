S = input("Enter the String: ")
dct = {}
for i in range(10):
    dct[i] = 0
for i in S:
    try:
        dct[int(i)]+=1
    except:
        pass
for k,v in dct.items():
    print(k," is print ",v," times.")

