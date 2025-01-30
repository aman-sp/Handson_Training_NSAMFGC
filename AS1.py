import numpy as np
n = int(input("Enter the number of array elements:"))
m = int(input("Enter the number of operations to be performed:"))
print(n, "\t", m)
arr = np.zeros(n)
print("Array sts as:",arr)
for i in range(m):
    st_in, en_in = map(int, input("\nEnter the sting and ending index:").split())
    num = int(input("Enter the number to be added:"))
    arr[st_in:en_in+1] += num
    print("Operation",i, ": Add ",num," from index ",st_in," to ",en_in,":",arr)

print("Maximum value in the final array is:",max(arr))
