#not finished
row_count=int(input("enter row count:"))
mat_tree=[[0 for i in range(row_count)] for j in range(row_count)]
for i in range(row_count):
   for j in range(row_count):
      if i>=j:
         mat_tree[i][j]=int(input("enter element"))
for i in range(row_count):
   for j in range(row_count):
      if i>=j:
         print(mat_tree[i][j],end=" ")
   print()
