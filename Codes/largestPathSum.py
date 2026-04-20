# Author - Hariharasudhan A

row_count = int(input("enter row count: "))
mat_tree = [[0 for i in range(row_count)] for j in range(row_count)] # initializing a dummy matrix with 0 

'''
in a lower triangular formed matrix representing a tree 
we should add all the nodes to find the largest path sum
and return it
'''

for i in range(row_count):
    for j in range(row_count):
        if i >= j: # lower triangular matrix criterion
            mat_tree[i][j] = int(input("enter element: "))
# display matrix tree
for i in range(row_count):
    for j in range(row_count):
        if i >= j:
            print(mat_tree[i][j], end=" ")
    print()
# dummy array with 0 for storing sum 
dp = [[0 for i in range(row_count)] for j in range(row_count)]
dp[0][0] = mat_tree[0][0]
for i in range(1, row_count):# iterate through every possible solution and find the sum
    for j in range(i + 1):      
        left  = dp[i-1][j-1] if j > 0 else -1
        above = dp[i-1][j]   if j < i else -1
        dp[i][j] = mat_tree[i][j] + max(left, above)
       
print("max sum =", max(dp[row_count-1][:row_count]))
