class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:

        mpp = {}

        for num in nums :
            if num in mpp:
                mpp[num] += 1
            else:
                mpp[num] = 1

        max_freq = max(mpp.values())

        count = 0 

        for freq in mpp.values() :
            if max_freq == freq :
                count += freq
        return count
        


        