# Longest Common Prefix

## Description

Finds the longest common prefix string among an array of strings by sorting the array and comparing only the first and last strings character by character.

## Approach

Sort the array of strings lexicographically. After sorting, the first and last strings are the most different from each other. Any prefix shared by all strings must also be shared between these two extremes. Compare the first and last strings character by character, appending matching characters to the result until a mismatch is found.

## Algorithm

```
ALGORITHM LONGEST_COMMON_PREFIX
// Finds the longest prefix shared by all strings in an array
// Input  : An array of strings strs
// Output : The longest common prefix string, or empty string if none

Sort strs lexicographically
Set result = empty string
Set i = 0
While i is less than length of strs[0]
    If character at position i of strs[0] equals character at position i of strs[last]
        Append that character to result
    Else
        Break
    Increment i
Return result
```

## Time Complexity

O(n log n · m) — sorting n strings dominates, where m is the length of the longest string.

## Code

[14.Longest Common Prefix.py](../Codes/14.Longest%20Common%20Prefix.py)

## Author


Hariharasudhan A
sophomore in CSE , MEPCO schlenk engineering college 
Sivakasi
reach me : sudanayyappann_bcs28@mepcoeng.ac.in
