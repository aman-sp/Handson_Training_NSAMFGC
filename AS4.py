def rot(mat,n):
    rot_mat = [[mat[n-1-j][i] for j in range(n)] for i in range(n)]
    return rot_mat

n=int(input("Enter the size of the matrix:"))
print("Enter the matrix row by row:")
mat=[list(map(int, input().split())) for _ in range(n)]
rot_mat = rot(mat,n)

print("\nRotated matrix:")
for row in rot_mat:
    print(" ".join(map(str,row)))

