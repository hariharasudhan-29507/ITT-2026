# Remove an Element

## Problem Description

Given an integer array `nums` and an integer `val`, remove **all occurrences** of `val` in `nums` **in-place**. The order of the remaining elements may change.

Return `k` — the number of elements in `nums` that are not equal to `val`. The first `k` elements of `nums` should hold the result.

This is LeetCode #27.

---

## Short Description

This program removes all occurrences of a given value (`val`) from an array (`nums`) in-place. It uses a **two-pointer approach** where one pointer (`x`) iterates through the array and another (`i`) tracks the position for the next valid element. It returns the count of elements that are not equal to `val`.

**Example:** `[3, 2, 2, 3]` with `val = 3` modifies the array to `[2, 2, ...]` and returns `2`.

---

## Approach: Two-Pointer (Fast/Slow)

- **Slow pointer** `i`: Points to the next position where a valid (non-`val`) element should be written.
- **Fast pointer** `x`: Iterates through every element in the array.

For each element `x`:
- If `x != val`, write it to `nums[i]` and increment `i`.
- If `x == val`, skip it.

At the end, `i` equals the count of valid elements, and the first `i` positions of `nums` contain the result.

---

## Code

```python
class Solution(object):
    def removeElement(self, nums, val):
        i = 0
        for x in nums:
            if x != val:
                nums[i] = x
                i += 1
        return i

s = Solution()
s.removeElement([3, 2, 2, 3], 3)  # Output: 2, nums = [2, 2, ...]
```

---

## Complexity Analysis

| Complexity | Value | Explanation |
|------------|-------|-------------|
| **Time**   | O(n)  | The loop iterates through every element in `nums` exactly once. All operations inside (comparison and assignment) are O(1). `n` is the length of the array. |
| **Space**  | O(1)  | No extra data structures are used. All modifications are done in-place on the original array. |

---

## Examples

| Input                  | val | Output k | nums (first k elements) |
|------------------------|-----|----------|--------------------------|
| `[3, 2, 2, 3]`         | `3` | `2`      | `[2, 2]`                |
| `[0,1,2,2,3,0,4,2]`   | `2` | `5`      | `[0,1,3,0,4]`           |
| `[1]`                  | `1` | `0`      | `[]`                    |
| `[4, 5]`               | `6` | `2`      | `[4, 5]`                |

---

## Edge Cases

- **val not in array**: No elements are removed; `i` equals the length of the array.
- **All elements equal val**: Every element is skipped; returns `0`.
- **Single element equal to val**: Returns `0`.
- **Empty array**: Loop never executes; returns `0`.

---

## Step-by-Step Walkthrough

For `nums = [3, 2, 2, 3]`, `val = 3`:

| Step | x | x != val? | nums after step        | i |
|------|---|-----------|------------------------|---|
| 1    | 3 | No        | `[3, 2, 2, 3]`         | 0 |
| 2    | 2 | Yes       | `[2, 2, 2, 3]`         | 1 |
| 3    | 2 | Yes       | `[2, 2, 2, 3]`         | 2 |
| 4    | 3 | No        | `[2, 2, 2, 3]`         | 2 |

Final result: `k = 2`, valid portion of `nums = [2, 2]`.

---

## Alternative Approaches

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Two-Pointer (this solution) | O(n) | O(1) | In-place; order may change for equal elements |
| Two-Pointer (swap from end) | O(n) | O(1) | Swap matched element with last element; fewer writes when val is rare |
| List comprehension (not in-place) | O(n) | O(n) | `[x for x in nums if x != val]` — creates a new list |

---

## Key Takeaways

- In-place removal avoids extra memory allocation, making this O(1) space.
- The two-pointer pattern is widely used in array manipulation problems (e.g., removing duplicates, partitioning arrays).
- The relative order of elements **not equal to val** is preserved in this implementation.
