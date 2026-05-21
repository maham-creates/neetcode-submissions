class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:


        hashset = {}
        for i in range(len(nums)):
            value = target - nums[i]
            if value in hashset:
                return [hashset[value],i]

            hashset[nums[i]] = i
