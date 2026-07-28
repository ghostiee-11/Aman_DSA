class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()

        largest1 = nums[-1]
        largest2 = nums[-2]

        return (largest1-1)*(largest2-1)
        