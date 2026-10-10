# 125. Valid Palindrome

- **Difficulty:** Easy
- **Tags:** Two Pointers, String
- **Link:** https://leetcode.com/problems/valid-palindrome/

## Problem

A phrase is a **palindrome** if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.



Given a string `s`, return `true`*if it is a **palindrome**, or*`false`*otherwise*.





**Example 1:**



```
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
```



**Example 2:**



```
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
```



**Example 3:**



```
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
```





**Constraints:**


 - `1 <= s.length <= 2 * 105`
 - `s` consists only of printable ASCII characters.

## Solutions

### Python3

- **Runtime:** 6 ms (beats 84.72%)
- **Memory:** 23.3 MB (beats 15.91%)
- **Submitted:** 2026-10-10 21:10 UTC

See [solution.py](solution.py).

## Notes

_Add your notes here._
