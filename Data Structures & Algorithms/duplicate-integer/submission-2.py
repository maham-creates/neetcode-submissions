class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for x in range(len(nums)):
            if nums[x] not in hashset:
                hashset.add(nums[x])
            else:
               return True
        return False
               

         