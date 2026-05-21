class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        pref = 1
        res = []*len(nums)
        for i in range(len(nums)):
            res.append(pref)
            pref = pref * nums[i]
        
        suff = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] = res[i]*suff
            suff = nums[i] * suff
        return res









        
        