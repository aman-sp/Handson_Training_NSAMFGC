def exist(bd,wrd):
    def dfs(bd,wrd,i,j,wrdInd):
        if wrdInd==len(wrd):
            return True
        if i<0 or i>=len(bd) or j<0 or j>=len(bd[0]) or bd[i][j]!=wrd[wrdInd]:
            return False
        temp=bd[i][j]
        bd[i][j]="#"
        if (
            dfs(bd,wrd,i+1,j,wrdInd+1)or
            dfs(bd,wrd,i-1,j,wrdInd+1)or
            dfs(bd,wrd,i,j+1,wrdInd+1)or
            dfs(bd,wrd,i,j-1,wrdInd+1)
        ):
            return True
        bd[i][j]=temp 
        return False
    for i in range(len(bd)):
        for j in range(len(bd[0])):
            if dfs(bd,wrd,i,j,0):
                return True
    return False
bd=[['A','B','C','E'],
    ['S','F','C','S'],
    ['A','D','E','E']]
wrd="ABCCED"
print(exist(bd,wrd))
