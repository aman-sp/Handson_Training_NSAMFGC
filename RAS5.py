def rev(s):
    if len(s)==0:
        return s
    else:
        return s[-1]+rev(s[:-1])

s=input("Enter the string:")
print("The reverse of",s,"is:",rev(s))