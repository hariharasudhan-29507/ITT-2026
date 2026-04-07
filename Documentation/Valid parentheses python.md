# Valid Parentheses

## Description

Validates whether a string containing bracket characters is properly matched and nested using a stack-based approach.

## Approach

Iterate through each character in the string. Push opening brackets onto a stack. When a closing bracket is encountered, check if the top of the stack holds the matching opening bracket. If at any point there is a mismatch or the stack is empty when a closing bracket is found, the string is invalid. After processing all characters, the string is valid only if the stack is empty.

## Algorithm

```
ALGORITHM VALID_PARENTHESES
// Checks if bracket characters in a string are correctly matched and nested
// Input  : A string s containing '(', ')', '{', '}', '[', ']'
// Output : True if all brackets are validly matched, False otherwise

Define mapping as {')': '(', '}': '{', ']': '['}
Initialize stack as empty list
For each character char in s
    If char is an opening bracket (i.e., char is in mapping values)
        Push char onto stack
    Else if char is a closing bracket (i.e., char is in mapping keys)
        If stack is empty OR mapping[char] does not equal top of stack
            Return False
        Else
            Pop the top of stack
Return True if stack is empty, else False
```

## Time Complexity

O(n) — each character in the string is processed exactly once.

## Code

[20.ValidParenthesis.py](../Codes/20.ValidParenthesis.py)

## Author

hariharasudhan
