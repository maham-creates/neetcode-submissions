class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        mapindex = {}
        
        i = 0

        while i < len(nums):
            num = target - nums[i]
            if num in mapindex:
                return [mapindex[num],i]

            mapindex[nums[i]] = i
            i += 1
        



        


        





                

        
