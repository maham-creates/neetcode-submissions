class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        pref = 1
        suff = 1
        res = [0]*len(nums)

        for i in range (len(nums)):
            res[i] = pref
            pref *= nums[i]
        
        for i in range(len(nums)-1,-1,-1):
            res[i] *= suff
            suff *= nums[i]
        return res
       


        
            



        