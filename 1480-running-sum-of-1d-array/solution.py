class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        res = []
        total = 0

        for i in range(len(nums)):
            total += nums[i]
            res.append(total)
        return res


        