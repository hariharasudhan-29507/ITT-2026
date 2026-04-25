# Remove Duplicates From Sorted Array

## Description

Removes duplicate elements from a sorted array in-place by converting it to a set, sorting the unique elements back, and returning the count of unique elements.

## Approach

Convert the array to a set to eliminate duplicates, then sort the resulting unique elements and write them back into the original array slice. Return the length of the unique elements as the new array size.

## Algorithm

```
ALGORITHM REMOVE_DUPLICATES_SORTED
// Removes duplicates from a sorted array in-place using set deduplication
// Input  : A sorted integer array nums
// Output : Integer k — the count of unique elements; nums modified in-place

Convert nums to a set to remove all duplicate values
Sort the unique values
Write the sorted unique values back into nums in-place
Return the count of unique elements
```

## Time Complexity

O(n log n) — dominated by sorting the unique elements.

## Code

[26.RemoveDuplicatesFromSortedArray.py](../Codes/26.RemoveDuplicatesFromSortedArray.py)

## Author

Hariharasudhan A  
sophomore in CSE , MEPCO schlenk engineering college  
Sivakasi  
reach me : sudanayyappann_bcs28@mepcoeng.ac.in
