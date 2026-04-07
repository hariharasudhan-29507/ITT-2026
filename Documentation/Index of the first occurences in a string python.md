# Index of the First Occurrence in a String

## Problem Description

Given two strings `haystack` and `needle`, return the index of the **first occurrence** of `needle` in `haystack`, or `-1` if `needle` is not part of `haystack`.

This is a classic string-searching problem (LeetCode #28).

---

## Approach: Sliding Window / Brute Force

The solution uses a simple sliding window technique:
- Iterate through every possible starting position `i` in `haystack`.
- At each position, extract a substring of the same length as `needle` using slicing: `haystack[i:i+len(needle)]`.
- If the slice matches `needle`, return the current index `i`.
- If no match is found after the full traversal, return `-1`.

---

## Code

```python
class Solution(object):
    def strStr(self, haystack, needle):
        lens = len(needle)
        for i in range(0, len(haystack)):
            if haystack[i:i+lens] == needle:
                return i
        return -1

s = Solution()
s.strStr("sadbutsad", "sad")  # Output: 0
```

---

## Complexity Analysis

Let `n` be the length of `haystack` and `m` be the length of `needle`.

| Complexity | Value | Explanation |
|------------|-------|-------------|
| **Time**   | O(n · m) | The outer loop runs `n` times. Each iteration performs a string slice and comparison, both O(m). In the worst case (e.g., `haystack = "aaaaa"`, `needle = "aab"`), the total work is O(n · m). |
| **Space**  | O(m) | Python slicing creates a new string object in memory. Each `haystack[i:i+lens]` temporarily occupies O(m) space. |

---

## Examples

| haystack       | needle | Output |
|----------------|--------|--------|
| `"sadbutsad"`  | `"sad"` | `0`   |
| `"leetcode"`   | `"leeto"` | `-1` |
| `"hello"`      | `"ll"` | `2`   |
| `""`           | `""` | `0`   |

---

## Edge Cases

- **Empty needle**: If `needle` is an empty string, return `0` (by convention).
- **needle longer than haystack**: The loop will never find a match; return `-1`.
- **Exact match**: If `haystack == needle`, return `0`.
- **No match**: Return `-1`.

---

## Alternative Approaches

| Approach | Time Complexity | Notes |
|----------|----------------|-------|
| Brute Force (this solution) | O(n · m) | Simple and readable |
| KMP Algorithm | O(n + m) | Optimal for repeated patterns; avoids re-checking characters |
| Rabin-Karp (Rolling Hash) | O(n + m) average | Hash-based; efficient in practice |
| Python built-in `find()` | O(n · m) worst | `haystack.find(needle)` — uses optimized C internals |

---

## Key Takeaways

- String slicing in Python is O(m) since it creates a new string.
- For interview settings, this brute force solution is acceptable for small inputs.
- For production or large inputs, consider KMP or the built-in `str.find()` / `str.index()` methods.
