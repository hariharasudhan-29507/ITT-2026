# Palindrome Number

## Problem Description

Given an integer `x`, return `True` if `x` is a **palindrome**, and `False` otherwise.

A number is a palindrome if it reads the same forwards and backwards (e.g., `121`, `1331`, `0`).

This is LeetCode #9.

---

## Approach: Digit Reversal

The solution reverses the integer mathematically (without converting to a string) and compares the reversed number to the original:

1. Save the original value of `x` into `n`.
2. Iteratively extract the last digit using `rem = n % 10`.
3. Build the reversed number: `temp = temp * 10 + rem`.
4. Shift `n` right by one digit: `n //= 10`.
5. After the loop, if `x == temp`, the number is a palindrome.

> **Note:** Negative numbers are never palindromes (e.g., `-121` reversed is `121-`).

---

## Code

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        n = x
        temp = 0
        while n > 0:
            rem = n % 10
            temp = (temp * 10) + rem
            n //= 10
        if x == temp:
            return True
        else:
            return False

s = Solution()
x = 121
print(s.isPalindrome(x))  # Output: True
```

---

## Complexity Analysis

| Complexity | Value | Explanation |
|------------|-------|-------------|
| **Time**   | O(log₁₀ n) | The `while` loop runs once per digit of `x`. Since we divide `n` by 10 each iteration, the loop runs log₁₀(n) times. |
| **Space**  | O(1) | Only three integer variables (`n`, `temp`, `rem`) are used, regardless of input size. |

---

## Examples

| Input  | Output  | Reason |
|--------|---------|--------|
| `121`  | `True`  | 121 reversed = 121 |
| `-121` | `False` | Negative numbers are not palindromes |
| `10`   | `False` | 10 reversed = 01 = 1 ≠ 10 |
| `0`    | `True`  | 0 reversed = 0 |
| `1221` | `True`  | 1221 reversed = 1221 |

---

## Edge Cases

- **Negative numbers**: The `while n > 0` condition means `temp` stays `0` for any negative `x`, so `x != 0` → returns `False`. This correctly identifies negatives as non-palindromes.
- **Zero**: `x = 0` → loop doesn't run → `temp = 0` → `0 == 0` → `True`.
- **Numbers ending in 0 (non-zero)**: e.g., `10` → reversed is `01 = 1` ≠ `10` → `False`.

---

## Alternative Approaches

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Digit Reversal (this solution) | O(log n) | O(1) | No string conversion |
| String Conversion | O(log n) | O(log n) | `str(x) == str(x)[::-1]` — simple but uses extra space |
| Half Reversal | O(log n) | O(1) | Only reverse half the digits for an early exit; slightly more optimal |

---

## Key Takeaways

- Reversing an integer mathematically avoids the overhead of string conversion.
- The algorithm naturally handles negative numbers because the `while n > 0` guard prevents processing of negative values, leaving `temp = 0 ≠ x`.
- The space complexity is O(1), making it ideal for memory-constrained environments.
