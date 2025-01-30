def rep(s):
    f = {}
    for ch in s:
        if ch in f:
            f[ch]+=1
        else:
            f[ch]=1
    for ch in s:
        if f[ch]==1:
            return ch
    return "Not found."
st=input("Enter the String:")
rst=rep(st)
print(rst)  