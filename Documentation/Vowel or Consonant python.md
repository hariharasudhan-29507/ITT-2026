# Vowel or Consonant

## Description

Checks whether a given character is a vowel or a consonant and prints the result.

## Approach

Read a single character from the user. Check if the character belongs to the set of vowels (a, e, i, o, u). If it does, print that the character is a vowel. Otherwise, print that it is a consonant.

## Algorithm

```
ALGORITHM VOWEL_OR_CONSONANT
// Determines if a character is a vowel or consonant
// Input  : A single character char
// Output : A message stating whether char is a vowel or a consonant

Read char from user
If char is found in "aeiou"
    Print "given char is vowel"
Else
    Print "given char is consonant"
```

## Time Complexity

O(1) — a single membership check against a fixed set of five vowels is performed.

## Code

[vowelConsonant.py](../Codes/vowelConsonant.py)

## Author

hariharasudhan
