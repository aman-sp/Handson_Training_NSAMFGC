def palin(sub):
    return sub==sub[::-1]
def partition(s):
    res=[]
    def backtrack(st, path):
        if st==len(s):
            res.append(path)
            return
        for end in range(st+1,len(s)+1):
            if palin(s[st:end]):
                backtrack(end,path+[s[st:end]])  
    backtrack(0,[])
    return res
s1 = "aab"
print("Output:",partition(s1))
