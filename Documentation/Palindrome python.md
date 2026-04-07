# Palindrome Number

## Description

Checks whether a given integer is a palindrome by reversing its digits mathematically and comparing the result to the original number. Negative numbers are never considered palindromes.

## Approach

Extract each digit from the right of the number using modulo and division, building a reversed number. After processing all digits, compare the reversed number to the original input.

## Algorithm

```
ALGORITHM PALINDROME_CHECK
// Determines if an integer is a palindrome by digit reversal
// Input  : An integer x
// Output : True if x is a palindrome, False otherwise

Set n = x
Set temp = 0
While n is greater than 0
    Set rem = n modulo 10
    Set temp = (temp * 10) + rem
    Set n = n divided by 10 (integer division)
If x equals temp
    Return True
Else
    Return False
```

## Time Complexity

O(log n) — the loop runs once per digit in the input number.

## Code

[9.Palindrome.py](../Codes/9.Palindrome.py)

## Author

hariharasudhan
