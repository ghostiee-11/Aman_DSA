class Solution:
    def reverseDegree(self, s: str) -> int:
        ans = 0

        for i, ch in enumerate(s):
            reverse_value = ord('z') - ord(ch) + 1
            ans += (i + 1) * reverse_value

        return ans