class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        frequency_counter = Counter(nums)

        max_frequency = max(frequency_counter.values())

        total_count = sum(freq for freq in frequency_counter.values() if freq == max_frequency)
        return total_count
        