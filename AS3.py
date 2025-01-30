def sub_arr(arr,tot,n):
    sum = 0
    st = 0
    for i in range(len(arr)):
        sum+=arr[i]
        while sum>tot and st<=i:
            sum-=arr[st]
            st+=1
        if sum==tot:
            return (st, i)
    return "Not found." 
arr=[]
n,tot=map(int,input("Enter the size of the array and the total sum of the array:").split())
arr = list(map(int, input("Enter the array elements:").split()))
rst=sub_arr(arr,tot,n)
print(rst)  



