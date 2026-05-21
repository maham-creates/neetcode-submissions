class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        num = set(nums)

        maximum = 0
        
        for val in num:
            if val - 1 not in num:
                length = 1
                while val + length in num:
                    length += 1
                maximum = max(length,maximum)
        
        return maximum
