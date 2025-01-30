def power(b,ex):
    if ex==0:
        return 1
    else:
        return b*power(b,ex-1)

b,ex=map(int,input("Enter the base and the exponent:").split())
rst=power(b, ex)
print(b,"to the power of",ex,"is:",rst)

