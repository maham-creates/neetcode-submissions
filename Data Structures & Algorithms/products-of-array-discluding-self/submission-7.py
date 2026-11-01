class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix = 1
        res = [0]*len(nums)
        
        i = 0
        while i < len(nums):
            res[i] = prefix
            i += 1
            prefix *= nums[i-1]
            
        suffix = 1
        j = len(nums) - 1
        while j >= 0:
            res[j] *= suffix
            suffix *= nums[j]
            j -= 1
        return res
            

        
            



        