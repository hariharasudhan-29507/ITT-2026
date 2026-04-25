# Hit and Guess

## Description

Compares a secret code string and a guess string character by character, returning a result string that marks each position as a hit (H) when the character matches exactly, or near (N) when the character exists somewhere in the code but not at the same position.

## Approach

Iterate through positions up to the length of the shorter string. For each position, check if the guess character exactly matches the code character at the same index — if so, record a hit. If not, check whether the guess character appears anywhere in the code — if so, record a near. Concatenate the position number with the result marker for each match found.

## Algorithm

```
ALGORITHM HIT_AND_GUESS
// Compares code and guess strings, marking hits and nears by position
// Input  : A code string str1 and a guess string str2
// Output : A result string of position-marker pairs (e.g., "0H2N")

Set result = empty string
Set l = minimum of length of str1 and length of str2
For i from 0 to l
    If str1[i] equals str2[i]
        Append i and "H" to result
    Else if str2[i] exists anywhere in str1
        Append i and "N" to result
Return result
```

## Time Complexity

O(n²) — for each of the n positions, checking if the character exists in the code string takes O(n) in the worst case.

## Code

[HitGuess.py](../Codes/HitGuess.py)

## Author


Hariharasudhan A
sophomore in CSE , MEPCO schlenk engineering college 
Sivakasi
reach me : sudanayyappann_bcs28@mepcoeng.ac.in
