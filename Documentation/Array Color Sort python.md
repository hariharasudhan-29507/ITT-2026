# Array Color Sort

## Description

Sorts an array of color codes (0 for red, 1 for blue, 2 for green) and prints the corresponding color names in sorted order.

## Approach

Sort the input array of integer color codes in ascending order. Iterate through the sorted array and print the color name corresponding to each code: 0 maps to red, 1 maps to blue, and 2 maps to green. If any code other than 0, 1, or 2 is encountered, print an error message and stop.

## Algorithm

```
ALGORITHM ARRAY_COLOR_SORT
// Sorts color codes and prints their color names
// Input  : An array of integers (0, 1, or 2) representing color codes
// Output : Color names printed in sorted order

Read array arr from user
Sort arr in ascending order
For each element in arr
    If element is 0
        Print "red"
    Else if element is 1
        Print "blue"
    Else if element is 2
        Print "green"
    Else
        Print error message and stop
```

## Time Complexity

O(n log n) — dominated by sorting the array of n elements.

## Code

[arrayColor.py](../Codes/arrayColor.py)

## Author

hariharasudhan
