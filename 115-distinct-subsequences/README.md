# 115. Distinct Subsequences

- **Difficulty:** Hard
- **Tags:** String, Dynamic Programming
- **Link:** https://leetcode.com/problems/distinct-subsequences/

## Problem

Given two strings s and t, return *the number of distinct* ***subsequences****of*s*which equals*t.



The test cases are generated so that the answer fits on a 32-bit signed integer.





**Example 1:**



```
Input: s = "rabbbit", t = "rabbit"
Output: 3
Explanation:
As shown below, there are 3 ways you can generate "rabbit" from s.
rabbbit
rabbbit
rabbbit
```



**Example 2:**



```
Input: s = "babgbag", t = "bag"
Output: 5
Explanation:
As shown below, there are 5 ways you can generate "bag" from s.
babgbag
babgbag
babgbag
babgbag
babgbag
```





**Constraints:**


 - `1 <= s.length, t.length <= 1000`
 - `s` and `t` consist of English letters.

## Solutions

### Python3

- **Runtime:** 903 ms (beats 7.66%)
- **Memory:** 232.5 MB (beats 15.32%)
- **Submitted:** 2026-09-06 18:50 UTC

See [solution.py](solution.py).

## Notes

_Add your notes here._
