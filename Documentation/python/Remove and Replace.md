# Remove and Replace

## Description

Removes all occurrences of a specific value from a list and replaces those removed positions at the end of the output with underscores, preserving the original list length visually.

## Approach

Iterate through the list and print each element that is not equal to the target value while counting how many valid elements were kept. After iterating, print underscores for each removed position to fill the remaining slots up to the original list length.

## Algorithm

```
ALGORITHM REMOVE_AND_REPLACE
// Removes a value from list and fills removed positions with underscores
// Input  : A list nums and an integer val to remove
// Output : Printed list with val removed and trailing underscores in place of removed elements

Read nums and val from user
Set l = length of nums
Set k = 0
Print opening bracket
For i from 0 to l
    If nums[i] is not equal to val
        Print nums[i]
        Increment k
For i from 0 to (l minus k)
    Print "_"
Print closing bracket
```

## Time Complexity

O(n) — the list is traversed once to print valid elements and once more to print underscores.

## Code

[removeReplace.py](../Codes/removeReplace.py)

## Author


Hariharasudhan A
sophomore in CSE , MEPCO schlenk engineering college 
Sivakasi
reach me : sudanayyappann_bcs28@mepcoeng.ac.in
