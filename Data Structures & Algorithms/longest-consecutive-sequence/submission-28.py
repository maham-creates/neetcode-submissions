class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0

        num_set = set(nums)
      
        maxseq = 0
        for num in num_set:
            length,i = 0,0
            if num - 1 not in num_set:
                while num + i in num_set:
                    length += 1
                    i += 1
                maxseq = max(maxseq,length)
        return maxseq

                

                


