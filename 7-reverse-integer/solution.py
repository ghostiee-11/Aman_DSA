class Solution:
    def reverse(self, x: int) -> int:
        s = str(abs(x)) [::-1]
        res = int(s) * (-1 if x<0 else 1)
        return res if -2**31<= res <= 2**31-1 else 0
        