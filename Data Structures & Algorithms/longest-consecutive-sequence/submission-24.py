class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        num_set = set(nums)
        maximum = 0
    
        for num in num_set:
            value = num -1
            if value not in num_set:
                length = 1
                while num + length in num_set:
                    length += 1
            
                maximum = max(length, maximum)
        return maximum

            
                

            
            




            
            

                


