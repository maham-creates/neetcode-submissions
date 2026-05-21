class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = {}
        for num in nums:
            freq[num] = 1 + freq.get(num,0)
        
        count = [[] for i in range(len(nums)+1)]
        for val, cnt in freq.items():
            count[cnt].append(val)
        
        res = []
        for i in range(len(count)-1,0,-1):
            for item in count[i]:
                res.append(item)
                if len(res) == k:
                    return res
        


        

