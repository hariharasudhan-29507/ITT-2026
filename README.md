# ITT-2026

A curated collection of **LeetCode solutions** and **custom Python programs** written during my sophomore year (ITT course). Problems are organised by ID or topic, and every file is self-contained with a small driver/test block so the output can be verified instantly.

---

## Repository Structure

```
ITT-2026/
├── Codes/           # Python source files (LeetCode + custom programs)
├── Documentation/   # PDF write-ups with descriptions, time & space complexity
└── README.md
```

---

## LeetCode Solutions

| Problem | LeetCode Link | Approach | File |
|---------|---------------|----------|------|
| Two Sum | [leetcode.com/problems/two-sum](https://leetcode.com/problems/two-sum/) | Brute-force nested loop – O(n²) | [1.TwoSum.py](https://github.com/hariharasudhan-29507/ITT-2026/blob/main/Codes/1.TwoSum.py) |
| Palindrome Number | [leetcode.com/problems/palindrome-number](https://leetcode.com/problems/palindrome-number/) | Integer reversal / string comparison | [9.Palindrome.py](https://github.com/hariharasudhan-29507/ITT-2026/blob/main/Codes/9.Palindrome.py) |
| Longest Common Prefix | [leetcode.com/problems/longest-common-prefix](https://leetcode.com/problems/longest-common-prefix/) | Character-by-character scan | [14.Longest Common Prefix.py](https://github.com/hariharasudhan-29507/ITT-2026/blob/main/Codes/14.Longest%20Common%20Prefix.py) |
| Valid Parentheses | [leetcode.com/problems/valid-parentheses](https://leetcode.com/problems/valid-parentheses/) | Stack-based matching | [20.ValidParenthesis.py](https://github.com/hariharasudhan-29507/ITT-2026/blob/main/Codes/20.ValidParenthesis.py) |
| Generate Parentheses | [leetcode.com/problems/generate-parentheses](https://leetcode.com/problems/generate-parentheses/) | DFS / backtracking | [22.GenerateParenthesis.py](https://github.com/hariharasudhan-29507/ITT-2026/blob/main/Codes/22.GenerateParenthesis.py) |
| Remove Duplicates from Sorted Array | [leetcode.com/problems/remove-duplicates-from-sorted-array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) | Two-pointer in-place | [26.RemoveDuplicatesFromSortedArray.py](https://github.com/hariharasudhan-29507/ITT-2026/blob/main/Codes/26.RemoveDuplicatesFromSortedArray.py) |
| Remove Element | [leetcode.com/problems/remove-element](https://leetcode.com/problems/remove-element/) | Two-pointer in-place | [27.RemoveElement.py](https://github.com/hariharasudhan-29507/ITT-2026/blob/main/Codes/27.RemoveElement.py) |
| Find Index of First Occurrence in String | [leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/) | Sliding window / built-in | [28.FindtheIndexoftheFirstOccurrenceinString.py](https://github.com/hariharasudhan-29507/ITT-2026/blob/main/Codes/28.FindtheIndexoftheFirstOccurrenceinString.py) |

---

## Custom Python Programs

| File | Description |
|------|-------------|
| `Arith.py` | Basic arithmetic operations demonstrating operator usage |
| `HitGuess.py` | Bulls-and-Cows style code-guessing game (Hit = correct position, Near = wrong position) |
| `Large3.py` | Finds the largest among three numbers using conditional logic |
| `OnlineStore.py` | Billing system that applies tiered discounts (1 % above ₹3 000, 2 % above ₹5 000) |
| `arrayColor.py` | Sorts/classifies array elements by colour category |
| `carBike.py` | Determines whether leftover tyres after bike purchases can form additional bikes |
| `chessMatch.py` | Calculates prize distribution for a 14-match chess tournament (C/N/D outcomes) |
| `coinGame.py` | Simulates a three-player coin game (Suresh, Sundar, Raja) with winner tracking |
| `countEven.py` | Counts even numbers in a collection |
| `largestPathSum.py` | Finds the maximum path sum in a triangle matrix using dynamic programming |
| `positivenegative.py` | Classifies a list of numbers into positive and negative groups |
| `removeReplace.py` | Removes or replaces specified elements in a list |
| `salaryTax.py` | Tax calculator with four slabs (≤2.5 L, 2.5–5 L, 5–10 L, >10 L) |
| `validIP.py` | Validates an IPv4 address (dot count, octet range 0–255) |
| `validMail.py` | Validates an email address (checks `@`, `.`, and illegal characters) |
| `vowelConsonant.py` | Classifies input characters as vowels or consonants |
| `withdraw.py` | Bank withdrawal simulation enforcing a ₹500 minimum balance and ₹100-multiple rule |

---

## Documentation

The `Documentation/` folder contains detailed PDF write-ups for selected problems, each covering:

- Problem description and constraints
- Step-by-step solution walkthrough
- **Time complexity** and **Space complexity** analysis

| PDF | Covers |
|-----|--------|
| `Palindrome python.pdf` | LeetCode #9 – Palindrome Number |
| `Longest common prefix python.pdf` | LeetCode #14 – Longest Common Prefix |
| `Valid parentheses python.pdf` | LeetCode #20 – Valid Parentheses |
| `Remove an element python.pdf` | LeetCode #27 – Remove Element |
| `Index of the first occurences in a string python.pdf` | LeetCode #28 – First Occurrence in String |

---

## Technical Specifications

| Attribute | Detail |
|-----------|--------|
| Language | Python 3+ |
| IDE / Editor | Any (VS Code recommended) |
| Focus | Data Structures & Algorithms, OOP, Input Validation |
| External Libraries | None (standard library only) |

---

## Getting Started

```bash
# Clone the repository
git clone https://github.com/hariharasudhan-29507/ITT-2026.git
cd ITT-2026/Codes

# Run any solution directly
python3 "1.TwoSum.py"
python3 validIP.py
```

> **Note:** Programs that use `input()` will prompt for values at runtime. LeetCode files have a small driver block at the bottom so they can be run standalone without any modifications.

---

## Purpose

* Strengthen problem-solving skills through daily LeetCode practice.
* Build real-world mini-projects (billing, banking, games) using Python OOP.
* Develop habits of documenting time and space complexity for every solution.

---

## About the Author

**A. Hariharasudhan**
Sophomore – B.E. Computer Science and Engineering
Mepco Schlenk Engineering College, Sivakasi
Reach me: sudanayyappan_bcs28@mepcoeng.ac.in

| | |
|---|---|
| Currently working on | Vehicle Rental and Booking System |
| Ask me about | Python, C++, Java, Oracle, MySQL |
| Reach me | sudanayyappan_bcs28@mepcoeng.ac.in |

