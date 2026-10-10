class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ''.join(ch.lower() for ch in s if ch.isalnum())

        pal =  res [::-1]

        return res == pal 