class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # convert array to hashset. No repetative values
        nums = set(nums)
        longest = 0
        for num in nums:
            if num - 1 not in nums:
                start_num = num
                count = 1
                
                while start_num + 1 in nums:
                    count+=1
                    start_num+=1
                longest = max(longest, count)
                    
                
        return longest

                
        