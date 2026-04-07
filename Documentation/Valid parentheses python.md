# Valid Parentheses

## Problem Description

Given a string `s` containing only the characters `'('`, `')'`, `'{'`, `'}'`, `'['`, and `']'`, determine if the input string is **valid**.

A string is valid if:
1. Every opening bracket has a corresponding closing bracket.
2. Opening brackets are closed in the **correct order**.
3. Every closing bracket closes the **most recently opened** unmatched bracket.

This is LeetCode #20.

---

## Description

An efficient solution using a **stack data structure** to ensure every opening bracket has a corresponding and correctly ordered closing bracket. The algorithm uses a dictionary for mapping bracket pairs, pushing opening brackets onto the stack and popping them when a matching closing bracket is encountered.

---

## Logic

1. **Opening bracket encountered** → push it onto the stack.
2. **Closing bracket encountered** → check if it matches the top of the stack:
   - If the stack is empty or the top doesn't match → return `False`.
   - Otherwise → pop the top of the stack.
3. **End of string** → if the stack is empty, the string is valid; otherwise, return `False`.

---

## Code

```python
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        mapping = {')': '(', '}': '{', ']': '['}
        stack = []

        for char in s:
            if char in mapping.values():   # Opening bracket
                stack.append(char)
            elif char in mapping:          # Closing bracket
                if not stack or mapping[char] != stack.pop():
                    return False
        return not stack
```

---

## Complexity Analysis

| Complexity | Value | Explanation |
|------------|-------|-------------|
| **Time**   | O(n)  | Single pass through the string `s` of length `n`. Each character is processed exactly once (one push or one pop). |
| **Space**  | O(n)  | In the worst case (all opening brackets), all `n` characters are pushed onto the stack. |

---

## Examples

| Input      | Output  | Reason |
|------------|---------|--------|
| `"()"`     | `True`  | Single matching pair |
| `"()[]{}"`  | `True`  | Multiple valid pairs |
| `"(]"`     | `False` | Mismatched brackets |
| `"([)]"`   | `False` | Incorrectly nested |
| `"{[]}"`   | `True`  | Correctly nested |
| `""`       | `True`  | Empty string is valid |
| `"("`      | `False` | Unclosed bracket |

---

## Edge Cases

- **Empty string**: No characters to process; stack remains empty → returns `True`.
- **Only closing brackets**: e.g., `")"` → stack is empty on pop → returns `False`.
- **Only opening brackets**: e.g., `"((("` → stack is non-empty at the end → returns `False`.
- **Single character**: Always `False` (can't be a valid pair).

---

## Step-by-Step Walkthrough

For `s = "{[]}"`:

| Step | char | Action         | Stack   |
|------|------|----------------|---------|
| 1    | `{`  | Push           | `[{]`   |
| 2    | `[`  | Push           | `[{, []` |
| 3    | `]`  | Pop `[` (match)| `[{]`   |
| 4    | `}`  | Pop `{` (match)| `[]`    |

Stack is empty → `True` ✅

For `s = "([)]"`:

| Step | char | Action              | Stack    |
|------|------|---------------------|----------|
| 1    | `(`  | Push                | `[(]`    |
| 2    | `[`  | Push                | `[(, []` |
| 3    | `)`  | Expects `(`, top is `[` → mismatch | — |

Returns `False` ❌

---

## The Mapping Dictionary

```python
mapping = {')': '(', '}': '{', ']': '['}
```

- Keys are **closing brackets**; values are their **matching opening brackets**.
- `mapping.values()` gives the set of opening brackets: `{'(', '{', '['}`.
- For a closing bracket `char`, `mapping[char]` gives its expected opening bracket.

---

## Alternative Approaches

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Stack with dictionary (this solution) | O(n) | O(n) | Clean and idiomatic |
| Stack with if-else | O(n) | O(n) | Verbose but avoids dictionary overhead |
| Counter (incorrect) | O(n) | O(1) | Only works for single bracket type; fails for mixed types |

---

## Key Takeaways

- The **stack** is the natural data structure for this problem because it enforces LIFO (Last-In, First-Out) ordering, which mirrors how brackets must be closed.
- Using a **dictionary** for bracket pairs makes the code concise and easy to extend to new bracket types.
- The `return not stack` idiom is Pythonic and ensures all opened brackets were properly closed.
