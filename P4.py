m=5
n=[50,15,80,10,5]
s=sum(n)
print(m,"\t",s)
for i in n:
    print(i)
def sup(s,z,n):
    for m in range(z):
        
        if s>n[m]:
            s-=n[m]
            print(n[m],"\t",n[m],"\t",0)
        elif s==0:      
            print(n[m],"\t",0,"\t",n[m])
        elif s<n[m]:
            print(n[m],"\t",s,"\t",n[m]-s)
            s=0
        
x=int(input("Enter the required order of eggs:"))
if x>=s:
    print("Sorry, we can supply ",s-1," eggs.")
    sup(s-1,m,n)
else:
    print("Thank you, your order for ",x," eggs are accepted.")
    sup(x,m,n)