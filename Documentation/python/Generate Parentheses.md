# Generate Parentheses

## Description

Generates all valid combinations of n pairs of parentheses using depth-first search with backtracking.

## Approach

Recursively build strings by tracking the count of open and close parentheses used so far. Add an opening parenthesis if the count of open brackets used is less than n. Add a closing parenthesis if the count of close brackets used is less than the count of open brackets. When the string length reaches 2*n, a valid combination is complete and added to the result list.

## Algorithm

```
ALGORITHM GENERATE_PARENTHESES
// Generates all valid n-pair parentheses combinations via backtracking
// Input  : An integer n representing the number of pairs
// Output : A list of all valid parentheses combination strings

Initialize result as empty list
Define recursive function DFS(left, right, current_string)
    If length of current_string equals n * 2
        Append current_string to result
        Return
    If left is less than n
        Call DFS(left + 1, right, current_string + '(')
    If right is less than left
        Call DFS(left, right + 1, current_string + ')')
Call DFS(0, 0, empty string)
Return result
```

## Time Complexity

O(4ⁿ / √n) — the number of valid combinations is the nth Catalan number.

## Code

[22.GenerateParenthesis.py](../Codes/22.GenerateParenthesis.py)

## Author

Hariharasudhan A  
sophomore in CSE , MEPCO schlenk engineering college  
Sivakasi  
reach me : sudanayyappann_bcs28@mepcoeng.ac.in
