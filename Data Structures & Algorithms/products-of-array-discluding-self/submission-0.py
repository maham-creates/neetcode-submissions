class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        product = [1]*n

        prefix = 1
        for x in range(n):
            product[x] = prefix
            prefix *= nums[x]

        postfix = 1
        for i in range(n-1,-1,-1):
            product[i] *= postfix
            postfix *= nums[i]

        return product
        