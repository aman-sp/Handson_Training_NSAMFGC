tup = (1,2,2,2,2,5,6,100,101)
def un_ele(tup):
    vis = []
    rst = []
    for ele in tup:
        if ele not in vis:
            vis+=[ele]  
            rst+=[ele] 
    return rst
print(un_ele(tup))