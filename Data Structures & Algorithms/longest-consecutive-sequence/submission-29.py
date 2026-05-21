class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        num_set = set(nums)
      
        maxseq = 0
        for num in num_set:
            length = 0
            if num - 1 not in num_set:
                while num + length in num_set:
                    length += 1
                maxseq = max(maxseq,length)
        return maxseq

                

                


