class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0

        # convert to a set to remove duplicates
        nums = set(nums)
        longest = 0

        for num in nums:
            if num - 1 not in nums:
                seq = 0
                while num + seq in nums:
                   seq += 1
                longest = max(seq,longest)
        return longest
           




            
            




        
