# Remove an Element

## Description

Removes all occurrences of a given value from an array in-place using a two-pointer technique, returning the count of remaining elements.

## Approach

Use a slow pointer to track the next write position and a fast pointer to scan every element. Whenever the current element does not match the value to remove, write it to the slow pointer position and advance the slow pointer. Elements equal to the target value are simply skipped.

## Algorithm

```
ALGORITHM REMOVE_ELEMENT
// Removes all occurrences of a target value from an array in-place
// Input  : An integer array nums and a target integer val
// Output : Integer k — count of elements in nums not equal to val

Set i = 0
For each element x in nums
    If x is not equal to val
        Set nums[i] = x
        Increment i
Return i
```

## Time Complexity

O(n) — each element in the array is visited exactly once.

## Code

[27.RemoveElement.py](../Codes/27.RemoveElement.py)

## Author

Hariharasudhan A  
sophomore in CSE , MEPCO schlenk engineering college  
Sivakasi  
reach me : sudanayyappann_bcs28@mepcoeng.ac.in
