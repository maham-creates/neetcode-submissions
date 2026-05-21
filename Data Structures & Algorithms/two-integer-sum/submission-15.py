class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashmap = {}
        for x in range(len(nums)):
            value = target - nums[x]
            if value in hashmap:
               return [hashmap[value],x]
            
            hashmap[nums[x]] = x
