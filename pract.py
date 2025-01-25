
import math
a = []
p=float(input("\nEnter the Principal Amount: "))
tp=int(input("Enter the time period: "))
for i in range(2):
    print("\nEnter the details of Bank", i + 1)
    ss = int(input("Enter the number of slabs:"))
    total = 0
    tt=0
    for j in range(ss):
        print("\nEnter the details of Slab",j + 1)
        yrs=int(input("Enter the tenure of slab: "))
        s=float(input("Enter the interest rate of Slab : "))
        tt+=yrs
        if(tp!=tt):
            print("Incorrect Input")
            break
        sq=pow((1+s),yrs*12)
        emi=(p*s)/(1-(1/sq))
        total+=emi
        print("EMI of Bank",i+1, "for Slab", j+1, "is:", emi)
    a.append(total)
    print("\nTotal EMI of Bank",i+1, "is:", total)
if a[0] < a[1]:
    print("Bank 1 offers the lesser EMI.")
elif a[0] > a[1]:
    print("Bank 2 offers the lesser EMI.")
else:
    print("Both banks offer the same EMI.")