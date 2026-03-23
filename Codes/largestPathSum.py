#not finished
row_count=int(input("enter row count:"))
sum_line=[]
line_val=0
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
for i in range(row_count):
    for j in range(row_count):
        if i>=j:
            k=0
            while k<row_count:
                print(mat_tree[j][k])
                line_val=line_val+mat_tree[i][k]
                k=k+1
            sum_line.append(line_val)
print(max(sum_line))   
