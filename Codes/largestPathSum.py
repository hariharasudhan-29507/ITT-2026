row_count = int(input("enter row count: "))
mat_tree = [[0 for i in range(row_count)] for j in range(row_count)]

for i in range(row_count):
    for j in range(row_count):
        if i >= j:
            mat_tree[i][j] = int(input("enter element: "))
for i in range(row_count):
    for j in range(row_count):
        if i >= j:
            print(mat_tree[i][j], end=" ")
    print()
dp = [[0 for i in range(row_count)] for j in range(row_count)]
dp[0][0] = mat_tree[0][0]
for i in range(1, row_count):
    for j in range(i + 1):      
        left  = dp[i-1][j-1] if j > 0 else -1
        above = dp[i-1][j]   if j < i else -1
        dp[i][j] = mat_tree[i][j] + max(left, above)
       
print("max sum =", max(dp[row_count-1][:row_count]))
