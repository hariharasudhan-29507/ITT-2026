# Longest Common Prefix

## Problem Description

Write a function to find the **longest common prefix** string among an array of strings. If there is no common prefix, return an empty string `""`.

This is a classic string problem (LeetCode #14).

---

## Approach: Sort and Compare

The solution leverages the observation that after **sorting** the array of strings lexicographically, the **first** and **last** strings will be the most dissimilar. Any prefix shared by all strings must therefore also be shared by these two extreme strings.

**Steps:**
1. Sort the input array `strs` lexicographically.
2. Compare the first string (`strs[0]`) and the last string (`strs[-1]`) character by character.
3. Build the common prefix as long as characters match.
4. Stop as soon as a mismatch is found or one string ends.

---

## Code

```python
class Solution(object):
    def longestCommonPrefix(self, strs):
        strs.sort()
        s = ""
        lens = len(strs)
        i = 0
        while i < len(strs[0]):
            if strs[0][i] == strs[lens - 1][i]:
                s += strs[0][i]
            else:
                break
            i = i + 1
        return s

s = Solution()
strs = ["flower", "flight", "flow"]
s.longestCommonPrefix(strs)  # Output: "fl"
```

---

## Complexity Analysis

Let `n` be the number of strings and `m` be the length of the longest string.

| Complexity | Value | Explanation |
|------------|-------|-------------|
| **Time**   | O(m · n log n) | Sorting `n` strings takes O(n log n) comparisons; comparing two strings of length `m` takes O(m). Total sort cost: O(m · n log n). The final comparison loop is at most O(m). |
| **Space**  | O(m) or O(n) | O(m) to store the resulting prefix. Python's Timsort also uses O(n) auxiliary space. |

---

## Examples

| Input                          | Output  |
|--------------------------------|---------|
| `["flower","flow","flight"]`   | `"fl"`  |
| `["dog","racecar","car"]`      | `""`    |
| `["interview","inter","internal"]` | `"inter"` |
| `["a"]`                        | `"a"`   |
| `["ab","a"]`                   | `"a"`   |

---

## Edge Cases

- **Single string**: The prefix is the string itself.
- **No common prefix**: Return `""`.
- **All identical strings**: The prefix equals any one of the strings.
- **Empty array**: Return `""` (handle defensively).
- **Empty string in array**: The common prefix is always `""`.

---

## Alternative Approaches

| Approach | Time Complexity | Notes |
|----------|----------------|-------|
| Sort and Compare (this solution) | O(m · n log n) | Clean and concise |
| Horizontal Scanning | O(m · n) | Compare prefix progressively across all strings |
| Vertical Scanning | O(m · n) | Compare column by column across all strings |
| Divide and Conquer | O(m · n) | Recursively split and merge; useful for parallel processing |
| Trie | O(m · n) build, O(m) query | Best for repeated prefix queries on the same set |

---

## Key Takeaways

- Sorting brings the lexicographically "furthest apart" strings to the front and back of the array, making it sufficient to only compare those two to find the common prefix.
- String concatenation in a loop (`s += char`) can be O(m²) in some languages; in Python, it is typically optimized, but `"".join(chars)` is more idiomatic.
- For large datasets with many prefix queries, a **Trie** data structure is the most efficient approach.
