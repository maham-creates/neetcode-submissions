class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}
        res = []

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        # frequency mapped to nums
        order = [[] for _ in range(len(nums)+1)] # buckets
        
        for key, val in count.items():
            order[val].append(key)
        
        #print(order)
        # [[], 9, 5, [], [], 10, [], 1, [], [], [], [], [], [], []]
        # [[], [], [7]]
        for i in range(len(order)-1,-1,-1):
            val = order[i]
            for num in val:
                res.append(num)
                if len(res) == k:
                    return res
                
                
            


       
        
            