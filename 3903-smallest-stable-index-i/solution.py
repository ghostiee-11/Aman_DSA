class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        for i in range (n) :
            mx = max(nums[:i+1])
            mn = min(nums[i:])

            if (mx - mn) <= k :
                return i

        return -1