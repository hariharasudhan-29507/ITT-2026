# Index of the First Occurrence in a String

## Description

Finds the index of the first occurrence of a needle string within a haystack string using a sliding window substring comparison. Returns -1 if the needle is not found.

## Approach

Iterate through every possible starting index in the haystack. At each position, extract a substring of the same length as the needle using slicing and compare it to the needle. Return the index immediately upon a match. If the loop completes without a match, return -1.

## Algorithm

```
ALGORITHM FIND_FIRST_OCCURRENCE
// Locates the starting index of the first occurrence of needle in haystack
// Input  : Two strings haystack and needle
// Output : Integer index of first occurrence, or -1 if not found

Set lens = length of needle
For i from 0 to length of haystack
    If substring of haystack from i to i+lens equals needle
        Return i
Return -1
```

## Time Complexity

O(n · m) — for each of the n positions in haystack, a substring comparison of length m is performed.

## Code

[28.FindtheIndexoftheFirstOccurrenceinString.py](../Codes/28.FindtheIndexoftheFirstOccurrenceinString.py)

## Author

Hariharasudhan A  
sophomore in CSE , MEPCO schlenk engineering college  
Sivakasi  
reach me : sudanayyappann_bcs28@mepcoeng.ac.in
