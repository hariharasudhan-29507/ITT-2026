# Count Even Numbers

## Description

Counts all even numbers from 1 to a given limit n and prints the total count.

## Approach

Read a number n from the user. If n is within the valid range (1 to 100000), iterate through every number from 1 to n and increment a counter whenever the number is divisible by 2. Print the final count. If n is outside the valid range, print an error message.

## Algorithm

```
ALGORITHM COUNT_EVEN_NUMBERS
// Counts all even numbers from 1 to n
// Input  : An integer n (1 to 100000)
// Output : The count of even numbers from 1 to n

Read n from user
If n is between 1 and 100000 (inclusive)
    Set count = 0
    For i from 1 to n (inclusive)
        If i is divisible by 2
            Increment count
    Print count
Else
    Print out of range error message
```

## Time Complexity

O(n) — the loop iterates through every number from 1 to n.

## Code

[countEven.py](../Codes/countEven.py)

## Author


Hariharasudhan A
sophomore in CSE , MEPCO schlenk engineering college 
Sivakasi
reach me : sudanayyappann_bcs28@mepcoeng.ac.in
