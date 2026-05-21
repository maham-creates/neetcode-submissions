class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        res = max(nums)   # cannot initialise to 0 because what if we had one number that is -1?
        curMin, curMax = 1, 1
      
        for n in nums: 
           tmp = curMax * n   # we wanna use old currMax to compute curMin
           curMax = max(n * curMax, n * curMin, n)
           curMin = min(tmp, n * curMin, n)
      
           res = max(res, curMax)
        return res

        