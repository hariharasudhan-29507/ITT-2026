# Largest Path Sum

## Description

Finds the maximum path sum from the top to the bottom of a lower-triangular matrix using dynamic programming, where each step moves either directly below or diagonally right.

## Approach

Read the lower-triangular matrix row by row. Build a dynamic programming table of the same size. The starting value is the single top element. For each subsequent row and column, the maximum reachable sum at that position is the element's value plus the larger of the two possible predecessor sums from the row above (either directly above or diagonally left-above). The answer is the maximum value in the last row of the DP table.

## Algorithm

```
ALGORITHM LARGEST_PATH_SUM
// Finds maximum sum path from top to bottom of a triangular matrix
// Input  : Number of rows and the lower-triangular matrix elements
// Output : The maximum path sum from the top row to the bottom row

Read row_count from user
Read and store lower-triangular matrix mat_tree
Initialize dp table of same size with all zeros
Set dp[0][0] = mat_tree[0][0]
For i from 1 to row_count
    For j from 0 to i (inclusive)
        Set left = dp[i-1][j-1] if j is greater than 0, else -1
        Set above = dp[i-1][j] if j is less than i, else -1
        Set dp[i][j] = mat_tree[i][j] plus maximum of left and above
Print the maximum value in the last row of dp
```

## Time Complexity

O(n²) — the lower-triangular matrix with n rows contains n(n+1)/2 cells total, each visited exactly once.

## Code

[largestPathSum.py](../Codes/largestPathSum.py)

## Author


Hariharasudhan A
sophomore in CSE , MEPCO schlenk engineering college 
Sivakasi
reach me : sudanayyappann_bcs28@mepcoeng.ac.in
