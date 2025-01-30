def gen_par(n):
    rst=[]
    def backtrack(c_str, o_cnt, c_cnt):
        if len(c_str) == 2 * n:
            rst.append(c_str)
            return
        if o_cnt<n:
            backtrack(c_str+"(",o_cnt+1,c_cnt)
        if c_cnt < o_cnt:
            backtrack(c_str+")",o_cnt,c_cnt+1)
    backtrack("",0,0)
    return rst
n = 3
print("Output:", gen_par(n))