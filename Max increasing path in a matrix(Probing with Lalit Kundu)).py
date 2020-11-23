"""
You are in a matrix where each cell has some coins placed on it. You can move in either of the 4 directions (up, left, right, bottom) 
where the movement is possible only if the cell you want to move to has strictly greater number of coins than your current cell. You can start from any cell. 
What is the maximum length of the path you can move?
"""
mat=[[0,1,2,1],[1,2,4,2],[0,1,6,7],[8,1,2,3]]

r=len(mat)-1
c=len(mat[0])-1
def calc(mat,i,j,curr_len):

    curr_len=curr_len+1
    adj_len=[]
    if j-1>=0:
        if mat[i][j-1]>mat[i][j]:
            next_len=calc(mat,i,j-1,curr_len)
            adj_len.append(next_len)
    if j+1<=c:

        if mat[i][j+1]>mat[i][j]:

            next_len=calc(mat,i,j+1,curr_len)
            adj_len.append(next_len)
    if i-1>=0:
        if mat[i-1][j]>mat[i][j]:
            next_len=calc(mat,i-1,j,curr_len)
            adj_len.append(next_len)
    if i+1<=r:
        if mat[i+1][j]>mat[i][j]:
            next_len=calc(mat,i+1,j,curr_len)
            adj_len.append(next_len)
    if len(adj_len)>0:
        return max(adj_len)
    return curr_len
        
curr_max=0
for i in range(r+1):
    for j in range(c+1):
        
        curr=calc(mat,i,j,0)
    
        if curr>curr_max:
            curr_max=curr
print(curr_max)
