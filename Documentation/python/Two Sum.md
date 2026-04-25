# Two Sum

## Description

Finds two indices in a list of integers whose values add up to a given target, returning the pair of indices.

## Approach

Use nested loops to check every pair of distinct elements. The outer loop picks the first element and the inner loop picks every subsequent element. When a pair whose sum equals the target is found, both indices are returned immediately.

## Algorithm

```
ALGORITHM TWO_SUM
// Finds two indices in an array whose values sum to target
// Input  : An integer array nums and an integer target
// Output : A list containing the two indices [i, j]

Initialize result as empty list
For i from 0 to length of nums
    For j from i+1 to length of nums
        If nums[i] + nums[j] equals target
            Append i to result
            Append j to result
            Return result
```

## Time Complexity

O(n²) — every pair of elements is considered in the worst case.

## Code

[1.TwoSum.py](../Codes/1.TwoSum.py)

## Author

Hariharasudhan A  
sophomore in CSE , MEPCO schlenk engineering college  
Sivakasi  
reach me : sudanayyappann_bcs28@mepcoeng.ac.in
