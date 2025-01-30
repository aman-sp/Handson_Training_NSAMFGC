n=int(input("Enter the value for n:"))
s1,s2,s3=input().split(" ")
for i in range(3,n):
    n4=int(s1)+int(s2)+int(s3)
    s1=int(s2)
    s2=int(s3)
    s3=n4
print("Sum is:",n4)